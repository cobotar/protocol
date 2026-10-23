#!/usr/bin/env python3
"""Verify that generated Python modules resolve from the package root."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--runtime",
        action="store_true",
        help="execute all generated module imports (requires package dependencies)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repository = Path(__file__).resolve().parents[1]
    source_root = repository / "src"
    package_root = source_root / "cobotar_protocol"
    generated_modules = sorted(
        ".".join(path.relative_to(source_root).with_suffix("").parts)
        for path in package_root.rglob("*_pb2.py")
    )
    assert generated_modules, "no generated Python modules found"
    protocol_roots = sorted({module.split(".", 2)[1] for module in generated_modules})

    subprocess.run(
        [
            sys.executable,
            str(repository / "scripts" / "rewrite_python_imports.py"),
            "--check",
        ],
        check=True,
    )

    code = f"""
import importlib
import importlib.util
import sys
from pathlib import Path

source_root = Path({str(source_root)!r})
package_root = Path({str(package_root)!r})
sys.path.insert(0, str(source_root))
assert str(package_root) not in sys.path

modules = {generated_modules!r}
protocol_roots = {protocol_roots!r}

for module in modules:
    spec = importlib.util.find_spec(module)
    assert spec is not None, module
    assert Path(spec.origin).is_relative_to(source_root), module
"""
    if args.runtime:
        code += """
for module in modules:
    importlib.import_module(module)
# The proto packages (common, product, runtime …) must only exist below cobotar_protocol.
top_level = sorted(name for name in sys.modules if name.split('.')[0] in protocol_roots)
assert not top_level, f'imported as top-level packages: {top_level}'
print(f'imported {len(modules)} generated modules from the package root')
"""
    subprocess.run([sys.executable, "-I", "-B", "-c", code], check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
