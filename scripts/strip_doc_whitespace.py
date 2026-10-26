#!/usr/bin/env python3
"""Strips trailing whitespace from the generated reference documentation.

The pseudomuto-doc plugin's markdown template leaves spaces at the end of blank and table lines, which
`git diff --check` reports. The plugin runs remotely, so its template can't be replaced here; `make generate`
cleans its output instead. Lines in this file never rely on a trailing double space for a line break.
"""

import pathlib
import sys

DEFAULT = pathlib.Path(__file__).resolve().parent.parent / "documentation" / "README.md"


def strip(path: pathlib.Path) -> bool:
    text = path.read_text(encoding="utf-8")
    cleaned = "\n".join(line.rstrip(" \t") for line in text.split("\n"))
    if cleaned != text:
        path.write_text(cleaned, encoding="utf-8")
        return True
    return False


if __name__ == "__main__":
    paths = [pathlib.Path(arg) for arg in sys.argv[1:]] or [DEFAULT]
    for path in paths:
        if strip(path):
            print(f"stripped trailing whitespace in {path}")
