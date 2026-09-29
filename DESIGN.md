---
name: OpenCCman website
description: Manuscript paper under an editor's red pencil, proofreading Chinese in three languages.
colors:
  paper: "#f7f9f6"
  sheet: "#ffffff"
  ink: "#1b2433"
  graphite: "#5b6472"
  rule-green: "#b7dac6"
  frame-green: "#2f8b63"
  green-ink: "#1f6e4c"
  green-wash: "#e6f1ea"
  red-pencil: "#cf3a2d"
  red-pencil-deep: "#b73024"
  red-wash: "#fbe5e1"
typography:
  display:
    fontFamily: "OpenCCman Serif SC / TC (Noto Serif subsets), Songti SC / TC, serif"
    fontSize: "0.72 × cell (69px in the 96px hero cell, 34.6px in the 48px cell)"
    fontWeight: 700
    lineHeight: "cell + 30% band"
  headline:
    fontFamily: "OpenCCman Serif SC / TC, Songti, serif"
    fontSize: "26px"
    fontWeight: 700
    lineHeight: 1.45
  title:
    fontFamily: "OpenCCman Serif SC / TC, Songti, serif"
    fontSize: "21px"
    fontWeight: 700
    lineHeight: 1.45
  lede:
    fontFamily: "-apple-system, PingFang SC / TC / HK, system-ui, sans-serif"
    fontSize: "20px"
    fontWeight: 400
    lineHeight: 1.85
  body:
    fontFamily: "-apple-system, PingFang SC / TC / HK, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.9
  hand:
    fontFamily: "OpenCCman Hand (LXGW WenKai subset), Kaiti, serif"
    fontSize: "0.44 × cell for corrections, 15–16px for margin notes"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "-apple-system, PingFang SC / TC / HK, system-ui, sans-serif"
    fontSize: "12–14px"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  hairline: "2px"
  stamp: "3px"
  frame: "6px"
  pill: "999px"
spacing:
  module: "48px (fluid below 1216px)"
  gutter: "32px (16px on phones)"
  section: "96px (2 modules)"
components:
  button-stamp:
    backgroundColor: "{colors.red-pencil}"
    textColor: "{colors.sheet}"
    rounded: "{rounded.stamp}"
    padding: "15px 24px 15px 22px"
  button-stamp-hover:
    backgroundColor: "{colors.red-pencil-deep}"
    textColor: "{colors.sheet}"
  preset-cell:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.graphite}"
    padding: "6px 11px"
  preset-cell-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.sheet}"
  language-cell-current:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    size: "34px"
  note:
    backgroundColor: "{colors.green-wash}"
    textColor: "{colors.ink}"
    rounded: "{rounded.hairline}"
    padding: "14px 18px"
  chip:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.graphite}"
    rounded: "{rounded.pill}"
    padding: "2px 9px"
---

# Design System: OpenCCman website

## Overview

**Creative North Star: "The Proofread Manuscript"**

Every page is a sheet of Chinese manuscript paper (稿纸) and OpenCCman is its proofreader. Display type sits one character per square cell on green ruling, the narrow band between rows belongs to corrections, and a red pencil circles what a conversion changed, marks with △ what a phrase kept, and writes the reason beside it. The proof desk on each home page runs this on real OpenCC 1.4.2 output, so the site demonstrates "phrase first, then form" instead of claiming it.

Reading pages stay calm: guides, changelog, support and privacy keep the paper, the ruled headings and the margin notes, and let long text run on plain paper at a comfortable measure. Density comes from typography and ruling, never from boxes. The world rejects device mockups, icon-tile feature grids, gradient bands and the old blue-and-system-type look.

**Key Characteristics:**
- Cool white paper ruled in manuscript green; blue-black ink; one red pencil.
- Three hands: a typeset serif for headings and results, a handwriting face for source text and corrections, the system sans for reading.
- Proofreading marks are the only icon system, each used for its real meaning.
- One authored motion (the pencil drawing its marks); everything else explains state.
- Light and dark are the same sheet by day and by night.

## Colors

A restrained manuscript palette: neutral paper and ink carry the page, green prints the structure, and red is the editor's pen.

### Primary
- **Red Pencil** (#cf3a2d; #ff7b6b on the night sheet): proof rings, △ keep marks, handwritten corrections and their reason tags, text-emphasis dots under changed characters, the candidate-release status, the support caution icon, and the ground of the one primary action. Contrast 4.6:1 on paper as text.
- **Deep Red Pencil** (#b73024): the pressed/hover state of the stamp button.

### Secondary
- **Frame Green** (#2f8b63; #5cbf8f at night): the masthead and colophon double rules, current-page underlines, focus rings, arrows and step numbers' cells.
- **Green Ink** (#1f6e4c; #7fd3a8 at night): small green text such as step numbers and the "released" status (5.9:1 on paper).
- **Rule Green** (#b7dac6; #2d4a3b at night): every cell line, row divider and hairline border.

### Neutral
- **Paper** (#f7f9f6; #121714 at night): the page ground, faintly green so the ruling feels printed on it.
- **Sheet** (#ffffff; #19211c at night): raised slips — the proof desk, feature figures, CTA sheet, support form slip.
- **Ink** (#1b2433; #e6ede8 at night): headings and body text (14.8:1).
- **Graphite** (#5b6472; #a3aea7 at night): captions, meta lines, summaries and pencil notes (5.7:1).
- **Green Wash** (#e6f1ea) and **Red Wash** (#fbe5e1): note backgrounds and hover tint; the red wash only flashes behind a character as it is typeset.

### Named Rules
**The Red Pencil Rule.** Red belongs to the editor: what changed, what still needs checking (a candidate release, a caution), and the page's one primary action, which a long page may repeat at its close. Never links, never decoration, never a competing second action.

**The Printed Structure Rule.** Structure is green and thin (1px). Anything that separates or frames content is ruling, not a colored slab.

## Typography

**Display Font:** OpenCCman Serif SC / TC — self-hosted subsets of Noto Serif SC and TC Bold (with Songti SC / TC, Noto Serif CJK, serif)
**Handwriting Font:** OpenCCman Hand — a self-hosted subset of LXGW WenKai (with Kaiti, BiauKai, serif)
**Body Font:** the system sans: -apple-system, PingFang SC / TC / HK, Microsoft YaHei / JhengHei, system-ui
**Latin display:** the SC subset's Latin (Source Serif forms), then Charter and Georgia

**Character:** The serif is the typesetter, the handwriting is the writer and the editor, the sans is the reader. English headings use the same serif's Latin, so the wordmark, version numbers and English titles read as one printed voice.

### Hierarchy
- **Display** (700, 0.72 × cell, one character per cell): page titles in 96px cells, section titles in 48px cells, the closing line.
- **Headline** (700, 26px, 1.45): feature names, guide section headings, CTA titles.
- **Title** (700, 21px, 1.45): guide titles in contents lists.
- **Lede** (400, 20px, 1.85; English 21px, 1.55): page introductions, at most 24em (Chinese) or 30em (English).
- **Body** (400, 17px, 1.9; English 1.65): reading text, at most 36em in Chinese and 34em in English; Chinese prose paragraphs indent two characters.
- **Hand** (400): corrections at 0.44 × cell above the ringed characters, margin glosses and pencil notes at 15–16px.
- **Label** (400–600, 12–14px): preset cells, captions, tags, meta.

### Named Rules
**The One Character, One Cell Rule.** Chinese display text sits exactly one character per square cell; a Latin run inside it spans whole cells; English text runs freely across the ruling. Full-row headings use 1-module or 2-module cells only, so every row stays whole at 24, 16 and 10 columns.

**The Three Hands Rule.** Source text and corrections are handwritten, results and headings are typeset, reading text is the system sans. A result row is never handwritten; a correction is never typeset.

## Layout

The page is laid out on a square module: 48px at 1216px and wider (24 modules, 1152px sheet), fluid 24 modules below that, 16 modules from 768px to 1023px, and 10 modules of the screen width minus 16px gutters on phones. Containers are always a whole number of modules, so cell headings end on a cell edge.

Home: the hero splits 10 + 13 modules (title, lede and stamp on the left, proof desk on the right, its top aligned to the first cell line), then feature rows of 9 + 13 modules (text beside a figure), the film plate at full width, the guides contents list, and a closing title in 96px cells. Reading pages put a sticky margin column (8 modules) beside a 14-module text column; the margin note comes first in the markup so phones read it before the steps. Everything collapses to one column below 1024px. Sections are separated by space (two modules), not boxes.

## Elevation & Depth

Paper is flat. Only loose slips lie on the sheet: the proof desk, the feature figures, the CTA sheet and the support form slip sit on the white sheet colour with a hairline green border; the proof desk and CTA sheet add a long, soft, offset shadow. The primary stamp carries a small coloured shadow of its own red.

### Shadow Vocabulary
- **Slip** (`box-shadow: 0 1px 2px rgb(27 36 51 / 0.05), 0 22px 44px -26px rgb(27 36 51 / 0.35)`): the proof desk.
- **Sheet** (`box-shadow: 0 18px 40px -30px rgb(27 36 51 / 0.4)`): the CTA sheet at the end of guides.
- **Stamp** (`box-shadow: 0 1px 1px rgb(27 36 51 / 0.08), 0 10px 22px -12px` the stamp red at 70%): the primary action only.

### Named Rules
**The Loose Slip Rule.** Only a slip that could be lifted off the page casts a shadow; ruling, notes and contents rows never do. At night shadows drop to black and do almost nothing, which is intended.

## Shapes

Square by default. Cells, preset tabs and language cells are hard squares that share their 1px borders. Slips and notes round to a 2px hairline, the stamp to 3px, window-like figure frames to 6px, chips to a pill. The TXT figure's files have one folded 14px corner. Proof marks are hand-drawn SVG loops that overshoot their start, never perfect ellipses.

## Components

### Buttons
- **Shape:** a seal-like stamp (3px radius) with a 1px inner frame inset 4px, like the border of a carved seal.
- **Primary (stamp):** Red Pencil ground, white 17px semibold label, an external-link arrow when it leaves the site (App Store, email). One action per page; the home page repeats the download stamp at its close.
- **Hover / Focus / Press:** deepens to Deep Red Pencil; presses 1px down with a tightened shadow in 120ms; focus shows the 2px Frame Green ring at 3px offset.
- **Secondary (slip link):** ink text with a green underline and a drawn arrow that moves 6px on hover.

### Preset cells and language cells
- **Style:** a row of cells sharing borders; unselected cells are Sheet with Graphite text, the selected one fills with Ink. Language cells (简 · 繁 · EN) are 34px squares with full names for assistive technology.
- **Behaviour:** native radio inputs under the cells, so arrow keys and screen readers work without script.

### Notes
- **Style:** Green Wash panel, 2px radius, a circled 注 / 註 (or a NOTE pill in English) as the proofreader's instruction mark. No coloured side stripe.

### Contents rows
- **Style:** numbered cells (the number is the recommended order), serif title, graphite summary, drawn arrow; rows separated by rule-green lines.
- **Hover:** a green wash sweeps the row, the number cell is ringed by the pencil, the arrow moves 6px.

### Proof desk (signature)
The home page's live demonstration. Preset cells on top; the source line in handwriting cells; red corrections in the band above each change; hand-drawn rings around changed segments (whole phrases for Taiwan terms, single characters for character forms), △ under characters a phrase kept, reason tags below; the typeset result line with text-emphasis dots under changed characters; a notes list that is also the accessible text; the caption "示例：OpenCC 1.4.2 的实际转换结果，并非 App 截图". Rings draw in 440ms with a 110ms stagger (70ms after interaction), corrections write left to right, the result characters settle; with reduced motion the marks simply appear.

### Film plate
The product video on its poster with green crop marks at two corners and a red hand-drawn ring around the play button; it loads only after a press, never autoplays or loops.

## Do's and Don'ts

### Do:
- **Do** generate every conversion from `scripts/specimens.py` (OpenCC 1.4.2) and label it as an example, not an app screenshot.
- **Do** keep full-row cell headings at 1 or 2 modules per cell so rows stay whole at every breakpoint.
- **Do** rerun `scripts/fonts.py` when headings, results or handwriting gain characters; `scripts/check.py` fails until the subsets cover them.
- **Do** use proofreading marks for their meanings only: ring = changed, △ = kept by a phrase, emphasis dot = changed in the result, circled 注 = note or limit, caret = something missing.
- **Do** keep motion to the pencil, state changes (page turns, layout toggles) and press feedback, and give each a reduced-motion path.

### Don't:
- **Don't** put an eyebrow or kicker above a heading; the imprint line lives in the masthead.
- **Don't** use red for links, decoration or a competing second action.
- **Don't** draw app or device chrome in figures: no traffic-light dots, bevelled keys or device frames.
- **Don't** add icon libraries, emoji or glyph icons; draw marks as SVG in the pencil stroke.
- **Don't** add inline styles, inline scripts, event-handler attributes, third-party fonts or third-party scripts; the site CSP is same-origin only.
