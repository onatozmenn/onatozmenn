"""Rewrite the recent pull requests block in README.md.

Reads the rendered markdown list on stdin and swaps it in between the
`prs:start` and `prs:end` markers, leaving the rest of the file alone.
"""

import pathlib
import re
import sys

MARKERS = re.compile(r"(<!-- prs:start -->).*?(<!-- prs:end -->)", re.DOTALL)

block = sys.stdin.read().strip() or "_Nothing recent._"
readme = pathlib.Path("README.md")
text = readme.read_text(encoding="utf-8")

if not MARKERS.search(text):
    sys.exit("README.md has no prs:start / prs:end markers")

readme.write_text(
    MARKERS.sub(lambda m: f"{m.group(1)}\n{block}\n{m.group(2)}", text),
    encoding="utf-8",
)
