"""Slice the vertical card fonts into files the browser loads on demand.

The vertical card tool draws whatever the visitor types, so it cannot use the
per-page subsets that fonts.py builds. Each face is cut into WOFF2 slices with a
unicode-range; the tool asks document.fonts.load() for the characters it is
about to draw and the browser fetches only the slices that cover them. Slice
membership follows Google Fonts' frequency grouping for Noto Serif SC / TC,
recorded in vertical_slices.json, so an ordinary sentence touches few files.

Coverage is GB 2312, Big5, ASCII and the punctuation blocks. A rarer character
falls back to the system serif on the canvas rather than inflating every slice.
The canvas rotates and places punctuation itself, so GSUB/GPOS are dropped.

Sources, all under the SIL Open Font License 1.1 (see site/assets/fonts/OFL.txt):

  Noto Serif SC / TC variable fonts, instanced at weight 400
      https://github.com/google/fonts/tree/main/ofl/notoserifsc
      https://github.com/google/fonts/tree/main/ofl/notoseriftc
  LXGW WenKai Regular
      https://github.com/lxgw/LxgwWenKai/releases

Build the slices (needs fonttools and brotli):

  python3 scripts/vertical_fonts.py --serif-sc 'NotoSerifSC[wght].ttf' \\
      --serif-tc 'NotoSerifTC[wght].ttf' --hand LXGWWenKai-Regular.ttf

Refresh the grouping from Google Fonts (network; the build itself is offline):

  python3 scripts/vertical_fonts.py --fetch-slices
"""

import json
import re
import shutil
import sys
from argparse import ArgumentParser
from concurrent.futures import ProcessPoolExecutor
from io import BytesIO
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
OUTPUT = SCRIPTS.parent / "site" / "assets" / "vertical"
SLICES = SCRIPTS / "vertical_slices.json"
MANIFEST = SCRIPTS / "vertical_fonts.json"
# key: (family, grouping in vertical_slices.json, variable weight to instance or None)
FACES = {
    "serif-sc": ("OpenCCman Card Serif SC", "sc", 400),
    "serif-tc": ("OpenCCman Card Serif TC", "tc", 400),
    "hand": ("OpenCCman Card Hand", "sc", None),
}
MIN_SLICE = 120  # adjacent rare groups merge until a slice holds at least this many characters
REST_SLICE = 400  # covered characters outside every Google group are chunked by code point
SAFARI = ("Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 "
          "(KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1")


def parse_range(text):
    points = set()
    for token in text.replace("U+", "").replace("u+", "").split(","):
        token = token.strip()
        if not token:
            continue
        if "?" in token:
            first, last = int(token.replace("?", "0"), 16), int(token.replace("?", "f"), 16)
        else:
            first, _, last = token.partition("-")
            first = int(first, 16)
            last = int(last, 16) if last else first
        points.update(range(first, last + 1))
    return points


def format_range(points):
    ordered = sorted(points)
    parts, start = [], ordered[0]
    for previous, current in zip(ordered, ordered[1:] + [None]):
        if current != previous + 1:
            parts.append(f"U+{start:x}" if start == previous else f"U+{start:x}-{previous:x}")
            start = current
    return ",".join(parts)


def fetch_slices():
    from datetime import date
    from urllib.request import Request, urlopen

    groups = {}
    for key, family in (("sc", "Noto+Serif+SC"), ("tc", "Noto+Serif+TC")):
        url = f"https://fonts.googleapis.com/css2?family={family}:wght@400&display=swap"
        css = urlopen(Request(url, headers={"User-Agent": SAFARI}), timeout=30).read().decode()
        groups[key] = re.findall(r"unicode-range:\s*([^;]+);", css)
        assert len(groups[key]) > 50, f"unexpected Google Fonts response for {family}"
    record = {"source": "Google Fonts CSS API v2 (Safari user agent), unicode-range order of each @font-face",
              "fetched": date.today().isoformat(), **groups}
    SLICES.write_text(json.dumps(record, indent=1) + "\n", encoding="utf-8")
    print(f"vertical_slices.json: {len(groups['sc'])} SC groups, {len(groups['tc'])} TC groups")


def coverage():
    """GB 2312, Big5, ASCII and the punctuation blocks a card can contain."""
    points = set(range(0x20, 0x7F)) | {0xA7, 0xB7, 0xD7, 0xF7}
    for first, last in ((0x2000, 0x206F), (0x2190, 0x21FF), (0x2460, 0x24FF), (0x25A0, 0x25FF),
                        (0x3000, 0x303F), (0xFE10, 0xFE1F), (0xFE30, 0xFE4F), (0xFF00, 0xFFEF)):
        points.update(range(first, last + 1))
    for codec, leads, trails in (("gb2312", range(0xA1, 0xF8), range(0xA1, 0xFF)),
                                 ("big5", range(0xA1, 0xFA), [*range(0x40, 0x7F), *range(0xA1, 0xFF)])):
        for lead in leads:
            for trail in trails:
                try:
                    points.update(map(ord, bytes((lead, trail)).decode(codec)))
                except UnicodeDecodeError:
                    pass
    return points


def plan(groups, available):
    """Google's groups restricted to the covered characters, rare groups merged, leftovers chunked."""
    slices, current, seen = [], set(), set()
    for text in groups:
        chars = (parse_range(text) & available) - seen
        seen |= chars
        current |= chars
        if len(current) >= MIN_SLICE:
            slices.append(current)
            current = set()
    rest = sorted(available - seen)
    if current:
        rest = sorted(current | set(rest))
    slices += [set(rest[i:i + REST_SLICE]) for i in range(0, len(rest), REST_SLICE)]
    return [chars for chars in slices if chars]


def rename(font, family):
    name = font["name"]
    for name_id in (16, 17, 21, 22, 25):
        name.removeNames(nameID=name_id)
    postscript = family.replace(" ", "") + "-Regular"
    for name_id, value in ((1, family), (2, "Regular"), (3, postscript), (4, f"{family} Regular"), (6, postscript)):
        name.setName(value, name_id, 3, 1, 0x409)
        name.setName(value, name_id, 1, 0, 0)


def options():
    from fontTools.subset import Options

    result = Options()
    result.layout_features = []
    result.hinting = False
    result.desubroutinize = True
    result.name_IDs = ["*"]
    result.name_languages = ["*"]
    result.drop_tables += ["DSIG", "vhea", "vmtx", "VORG"]
    return result


_BASE = None


def _init(base):
    global _BASE
    _BASE = base


def _slice(job):
    from fontTools.subset import Subsetter
    from fontTools.ttLib import TTFont

    path, points = job
    font = TTFont(BytesIO(_BASE))
    subsetter = Subsetter(options())
    subsetter.populate(unicodes=points)
    subsetter.subset(font)
    font.flavor = "woff2"
    font.save(path)
    return path.stat().st_size


def build(key, source, groups):
    from fontTools.subset import Subsetter
    from fontTools.ttLib import TTFont
    from fontTools.varLib.instancer import instantiateVariableFont

    family, grouping, weight = FACES[key]
    font = TTFont(source)
    if weight is not None and "fvar" in font:
        font = instantiateVariableFont(font, {"wght": weight})
    rename(font, family)
    available = coverage() & set(font.getBestCmap())
    # Cut the face down to the covered characters once, so every slice starts from a smaller font.
    base = Subsetter(options())
    base.populate(unicodes=available)
    base.subset(font)
    buffer = BytesIO()
    font.save(buffer)

    folder = OUTPUT / key
    shutil.rmtree(folder, ignore_errors=True)
    folder.mkdir(parents=True)
    slices = plan(groups[grouping], available)
    jobs = [(folder / f"{index}.woff2", sorted(chars)) for index, chars in enumerate(slices)]
    with ProcessPoolExecutor(initializer=_init, initargs=(buffer.getvalue(),)) as pool:
        sizes = list(pool.map(_slice, jobs))
    rules = [
        f'@font-face{{font-family:"{family}";src:url("{key}/{index}.woff2") format("woff2");'
        f"unicode-range:{format_range(chars)};font-weight:400;font-display:block}}"
        for index, chars in enumerate(slices)
    ]
    print(f"{key}: {len(available)} characters, {len(slices)} slices, {sum(sizes) / 1048576:.1f} MiB")
    return rules, {"family": family, "characters": len(available), "slices": len(slices), "bytes": sum(sizes)}


def main():
    parser = ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--fetch-slices", action="store_true")
    parser.add_argument("--serif-sc")
    parser.add_argument("--serif-tc")
    parser.add_argument("--hand")
    args = parser.parse_args()
    if args.fetch_slices:
        fetch_slices()
        return
    sources = {"serif-sc": args.serif_sc, "serif-tc": args.serif_tc, "hand": args.hand}
    if not all(sources.values()):
        parser.error("pass --serif-sc, --serif-tc and --hand, or --fetch-slices")
    groups = json.loads(SLICES.read_text(encoding="utf-8"))
    manifest = {}
    # One stylesheet per face: the tool links only the faces the chosen font needs.
    for key, source in sources.items():
        rules, manifest[key] = build(key, source, groups)
        header = "/* Generated by scripts/vertical_fonts.py; SIL OFL 1.1, see /assets/fonts/OFL.txt */"
        (OUTPUT / f"{key}.css").write_text("\n".join([header, *rules]) + "\n", encoding="utf-8")
    (OUTPUT / "fonts.css").unlink(missing_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
