"""Subset the self-hosted fonts to the characters the pages use.

Run build_site.py first: it records every display and handwriting character in
font_glyphs.json. This script needs fonttools and brotli plus the source fonts,
all released under the SIL Open Font License 1.1:

  Noto Serif SC / TC variable fonts
      https://github.com/google/fonts/tree/main/ofl/notoserifsc
      https://github.com/google/fonts/tree/main/ofl/notoseriftc
  LXGW WenKai Regular
      https://github.com/lxgw/LxgwWenKai/releases

The subsets are renamed "OpenCCman Serif SC/TC" and "OpenCCman Hand" and keep
the original copyright and licence records. A Traditional character missing from
Noto Serif TC (OpenCC's 爲, for one) is added to the SC subset instead, which the
Traditional font stack falls back to. check.py compares font_glyphs.json with
font_coverage.json, so a heading that needs a new character fails the check until
this script runs again.
"""

import json
from argparse import ArgumentParser
from pathlib import Path

from fontTools.subset import Options, Subsetter
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

SCRIPTS = Path(__file__).resolve().parent
OUTPUT = SCRIPTS.parent / "site" / "assets" / "fonts"
COVERAGE = SCRIPTS / "font_coverage.json"
# Latin, digits and the punctuation any heading may use, so edits rarely need a rebuild.
BASE = "".join(chr(c) for c in range(0x20, 0x7F)) + "·—–‘’“”…、。，：；！？「」『』（）《》〈〉＋"
FACES = {
    "serif-sc": ("OpenCCman Serif SC", "Bold", 700),
    "serif-tc": ("OpenCCman Serif TC", "Bold", 700),
    "hand": ("OpenCCman Hand", "Regular", None),
}


def rename(font, family, style):
    name = font["name"]
    for name_id in (16, 17, 21, 22):
        name.removeNames(nameID=name_id)
    postscript = family.replace(" ", "") + "-" + style
    for name_id, value in ((1, family), (2, style), (3, postscript), (4, f"{family} {style}"), (6, postscript)):
        name.setName(value, name_id, 3, 1, 0x409)
        name.setName(value, name_id, 1, 0, 0)


def subset(source, key, text):
    family, style, weight = FACES[key]
    font = TTFont(source)
    options = Options()
    options.hinting = False
    options.desubroutinize = True
    options.name_IDs = ["*"]
    options.name_languages = ["*"]
    subsetter = Subsetter(options)
    subsetter.populate(text=text + BASE)
    subsetter.subset(font)
    if "fvar" in font:
        font = instantiateVariableFont(font, {"wght": weight})
    for table in ("STAT", "DSIG"):
        if table in font:
            del font[table]
    rename(font, family, style)
    font.flavor = "woff2"
    target = OUTPUT / f"{key}.woff2"
    font.save(target)
    covered = "".join(sorted(chr(code) for code in TTFont(target).getBestCmap()))
    print(f"{target.relative_to(SCRIPTS.parent)}: {len(covered)} characters, {target.stat().st_size / 1024:.1f} KiB")
    return covered


def main():
    parser = ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--serif-sc", required=True, help="Noto Serif SC variable TTF")
    parser.add_argument("--serif-tc", required=True, help="Noto Serif TC variable TTF")
    parser.add_argument("--hand", required=True, help="LXGW WenKai Regular TTF")
    args = parser.parse_args()
    needed = json.loads((SCRIPTS / "font_glyphs.json").read_text(encoding="utf-8"))
    OUTPUT.mkdir(parents=True, exist_ok=True)
    coverage = {"serif-tc": subset(args.serif_tc, "serif-tc", needed["serif-tc"])}
    borrowed = "".join(sorted(set(needed["serif-tc"]) - set(coverage["serif-tc"])))
    coverage["serif-sc"] = subset(args.serif_sc, "serif-sc", needed["serif-sc"] + borrowed)
    coverage["hand"] = subset(args.hand, "hand", needed["hand"])
    COVERAGE.write_text(json.dumps(coverage, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    if borrowed:
        print(f"serif-tc borrows {borrowed} from serif-sc")
    for key in FACES:
        pool = set(coverage[key]) | (set(coverage["serif-sc"]) if key == "serif-tc" else set())
        lacking = "".join(sorted(set(needed[key]) - pool))
        if lacking:
            print(f"warning: no subset carries {lacking} for {key}; those characters use the fallback stack")


if __name__ == "__main__":
    main()
