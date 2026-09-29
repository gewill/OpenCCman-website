"""Generate the proof-desk specimens from real OpenCC 1.4.2 output.

Every converted string comes from the opencc CLI, which is the engine the app
embeds. OpenCC's own dictionaries only decide where a segment starts and why it
changed:

  char    the character's default form (first STCharacters candidate)
  phrase  a phrase entry chose a form the character default would not
  keep    a phrase entry kept a one-to-many character unchanged
  twp     Taiwan phrase stage (TWPhrases)
  twv     Taiwan variant stage (TWVariants)
  hkv     Hong Kong variant stage (HKVariants)

The app's presets map to OpenCC configs as t2s (Simplified), s2t (Traditional ·
OpenCC), s2twp (Taiwan) and s2hk (Hong Kong); see ConversionConfiguration.swift
in the app repository.
"""

import json
import os
import re
import shutil
import subprocess
import tempfile
from argparse import ArgumentParser
from pathlib import Path

OUTPUT = Path(__file__).resolve().parent / "specimens.json"
ENGINE = "1.4.2"
PRESETS = ("s2t", "s2twp", "s2hk", "t2s")
STAGE2 = {"s2twp": "t2tw", "s2hk": "t2hk"}
DICTS = ("STCharacters", "STPhrases", "STPhrases_GeneratedFromRegionalPhrases", "TSCharacters",
         "TSPhrases", "TWPhrases", "TWVariantsPhrases", "HKVariantsPhrases")
SPECIMENS = [
    ("mouse", "用鼠标打开软件里的视频"),
    ("queen", "皇后后天只有一只猫"),
    ("hair", "头发里发现了什么"),
    ("line", "他说为了这条线着急"),
    ("printer", "打印机内存不够"),
    ("noodle", "他们一起吃面"),
    ("bed", "床上的温度计"),
]


def available():
    """The installed OpenCC version, or None when the CLI is missing."""
    if not shutil.which("opencc"):
        return None
    run = subprocess.run(["opencc", "--version"], capture_output=True, text=True)
    match = re.search(r"Version:\s*(\S+)", run.stdout + run.stderr)
    return match.group(1) if match else "unknown"


def data_dir():
    candidates = [os.environ.get("OPENCC_DATA_DIR"), "/opt/homebrew/share/opencc",
                  "/usr/local/share/opencc", "/usr/share/opencc"]
    for candidate in candidates:
        if candidate and (Path(candidate) / "s2t.json").exists():
            return Path(candidate)
    raise SystemExit("OpenCC data directory not found; set OPENCC_DATA_DIR")


class Engine:
    def __init__(self, share, dicts):
        self.share = share
        self.cache = {}
        self.st_chars = dicts["STCharacters"]
        self.st_phrases = {**dicts["STPhrases"], **dicts["STPhrases_GeneratedFromRegionalPhrases"]}
        self.ts_chars = dicts["TSCharacters"]
        self.ts_phrases = dicts["TSPhrases"]
        self.tw_keys = set(dicts["TWPhrases"]) | set(dicts["TWVariantsPhrases"])
        self.hk_keys = set(dicts["HKVariantsPhrases"])

    def convert(self, config, text):
        key = (config, text)
        if key not in self.cache:
            run = subprocess.run(["opencc", "-c", str(self.share / f"{config}.json")], input=text,
                                 capture_output=True, text=True, check=True)
            self.cache[key] = run.stdout.rstrip("\n")
        return self.cache[key]


def load_dicts(share, workdir):
    tables = {}
    for name in DICTS:
        target = Path(workdir) / f"{name}.txt"
        subprocess.run(["opencc_dict", "-i", str(share / f"{name}.ocd2"), "-o", str(target),
                        "-f", "ocd2", "-t", "text"], check=True, capture_output=True)
        table = {}
        for line in target.read_text(encoding="utf-8").splitlines():
            if line:
                word, forms = line.split("\t")
                table[word] = forms.split(" ")
        tables[name] = table
    return tables


def mmseg(text, keys):
    longest = max(len(k) for k in keys)
    out, i = [], 0
    while i < len(text):
        for size in range(min(longest, len(text) - i), 0, -1):
            word = text[i:i + size]
            if size == 1 or word in keys:
                out.append(word)
                i += size
                break
    return out


def merge_spans(segs, stage_text, keys):
    """Join source segments that a later-stage phrase match spans."""
    pos = 0
    for word in mmseg(stage_text, keys):
        if len(word) > 1 and word in keys:
            start, end = pos, pos + len(word)
            merged, at, buf = [], 0, ""
            for seg in segs:
                lo, hi = at, at + len(seg)
                at = hi
                if hi <= start or lo >= end:
                    if buf:
                        merged.append(buf)
                        buf = ""
                    merged.append(seg)
                else:
                    buf += seg
            if buf:
                merged.append(buf)
            segs = merged
        pos += len(word)
    return segs


def default(text, chars):
    return "".join(chars.get(ch, [ch])[0] for ch in text)


def classify(cc, seg, out, preset):
    if preset == "t2s":
        if out == seg:
            return "same", None
        chardef = default(seg, cc.ts_chars)
        if len(seg) > 1 and seg in cc.ts_phrases and out != chardef:
            return "phrase", chardef
        return "char", None
    chardef = default(seg, cc.st_chars)
    if out == seg:
        multi = any(len(cc.st_chars.get(ch, [ch])) > 1 for ch in seg)
        if len(seg) > 1 and seg in cc.st_phrases and multi:
            alt = cc.convert(STAGE2[preset], chardef) if preset in STAGE2 else chardef
            return "keep", alt if alt != seg else None
        return "same", None
    st = cc.convert("s2t", seg)
    if preset == "s2twp" and out != cc.convert("s2tw", seg):
        return "twp", None
    if len(seg) > 1 and seg in cc.st_phrases and st != chardef:
        alt = cc.convert(STAGE2[preset], chardef) if preset in STAGE2 else chardef
        return "phrase", alt if alt != out else None
    if preset == "s2twp" and out != st:
        return "twv", None
    if preset == "s2hk" and out != st:
        return "hkv", None
    return "char", None


def split_marks(cc, row, preset):
    """Character-level kinds become one mark per changed character."""
    seg, out, kind = row["s"], row["o"], row["k"]
    if kind == "keep":
        table = cc.ts_chars if preset == "t2s" else cc.st_chars
        row["keep"] = [i for i, ch in enumerate(seg) if len(table.get(ch, [ch])) > 1]
        return [row]
    if kind not in ("char", "twv", "hkv", "same") or len(seg) != len(out) or len(seg) == 1:
        return [row]
    st = cc.convert("s2t", seg) if preset in ("s2twp", "s2hk") else out
    parts = []
    for i, (a, b) in enumerate(zip(seg, out)):
        if a == b:
            parts.append({"s": a, "o": b, "k": "same"})
        elif kind in ("twv", "hkv") and st[i] != b:
            parts.append({"s": a, "o": b, "k": kind})
        else:
            parts.append({"s": a, "o": b, "k": "char"})
    return parts


def variants(cc, base):
    result = {}
    for preset in PRESETS:
        src = cc.convert("s2t", base) if preset == "t2s" else base
        whole = cc.convert(preset, src)
        if preset == "t2s":
            segs = mmseg(src, set(cc.ts_phrases))
        else:
            segs = mmseg(src, set(cc.st_phrases))
            stage1 = cc.convert("s2t", src)
            assert len(stage1) == len(src), (src, stage1)
            if preset == "s2twp":
                segs = merge_spans(segs, stage1, cc.tw_keys)
            if preset == "s2hk":
                segs = merge_spans(segs, stage1, cc.hk_keys)
        rows = []
        for seg in segs:
            out = cc.convert(preset, seg)
            kind, alt = classify(cc, seg, out, preset)
            row = {"s": seg, "o": out, "k": kind}
            if alt:
                row["alt"] = alt
            rows.extend(split_marks(cc, row, preset))
        assert "".join(r["o"] for r in rows) == whole, f"{preset} {base}: segments disagree with OpenCC"
        result[preset] = {"src": src, "out": whole, "segs": rows}
    return result


def generate():
    share = data_dir()
    with tempfile.TemporaryDirectory() as workdir:
        cc = Engine(share, load_dicts(share, workdir))
        data = {"engine": f"OpenCC {ENGINE}", "specimens": []}
        for key, base in SPECIMENS:
            data["specimens"].append({"id": key, "base": base, "variants": variants(cc, base)})
        taiwan = cc.convert("s2twp", dict(SPECIMENS)["mouse"])
        data["taiwanToSimplified"] = {"src": taiwan, "out": cc.convert("t2s", taiwan)}
    return json.dumps(data, ensure_ascii=False, indent=1) + "\n"


def run(check=False):
    version = available()
    if version != ENGINE:
        message = "not installed" if version is None else f"version {version}"
        if check:
            print(f"SKIP specimens: OpenCC {ENGINE} is needed to verify them ({message})")
            return
        raise SystemExit(f"OpenCC {ENGINE} is required ({message})")
    content = generate()
    if check:
        assert OUTPUT.read_text(encoding="utf-8") == content, "specimens.json differs from OpenCC; run scripts/specimens.py"
    else:
        OUTPUT.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--check", action="store_true")
    run(check=parser.parse_args().check)
