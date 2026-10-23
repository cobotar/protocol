#!/usr/bin/env python3
"""Namespace imports in generated Python protobuf modules.

The protobuf generators emit imports relative to proto paths, such as
``from common.v1 import time_pb2``. The generated files are packaged below
``cobotar_protocol``, so those imports must use that package as their root.
External imports such as ``buf.validate`` and ``google.protobuf`` are left
unchanged.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


IMPORT_RE = re.compile(
    r"^(?P<prefix>\s*(?:from|import)\s+)"
    r"(?P<module>[A-Za-z_][A-Za-z0-9_.]*)"
    r"(?P<suffix>.*)$"
)


def generated_domains(package_root: Path) -> set[str]:
    """Return top-level proto packages generated below package_root."""
    return {
        child.name
        for child in package_root.iterdir()
        if child.is_dir() and any(child.rglob("*_pb2.py"))
    }


def rewrite_text(text: str, domains: set[str]) -> str:
    rewritten: list[str] = []
    for line in text.splitlines(keepends=True):
        content = line.rstrip("\r\n")
        ending = line[len(content) :]
        match = IMPORT_RE.match(content)
        if match and match.group("module").split(".", 1)[0] in domains:
            content = (
                f"{match.group('prefix')}cobotar_protocol."
                f"{match.group('module')}{match.group('suffix')}"
            )
        rewritten.append(content + ending)
    return "".join(rewritten)


def rewrite_package(package_root: Path, *, check: bool) -> list[Path]:
    domains = generated_domains(package_root)
    changed: list[Path] = []
    for path in sorted((*package_root.rglob("*.py"), *package_root.rglob("*.pyi"))):
        original = path.read_text(encoding="utf-8")
        rewritten = rewrite_text(original, domains)
        if rewritten == original:
            continue
        changed.append(path)
        if not check:
            path.write_text(rewritten, encoding="utf-8")
    return changed


def main() -> int:
    default_root = Path(__file__).resolve().parents[1] / "src" / "cobotar_protocol"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package_root", nargs="?", type=Path, default=default_root)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report imports that need rewriting without changing files",
    )
    args = parser.parse_args()

    changed = rewrite_package(args.package_root.resolve(), check=args.check)
    if args.check and changed:
        for path in changed:
            print(f"generated Python import needs rewriting: {path}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
