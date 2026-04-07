#!/usr/bin/env python3
"""Validate a Harness module from the skill bundle."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from harness_core import validate_module  # noqa: E402


def _safe_print(text: str) -> None:
    try:
        print(text)
    except UnicodeEncodeError:
        sys.stdout.buffer.write(text.encode(sys.stdout.encoding or "utf-8", errors="replace"))
        sys.stdout.buffer.write(b"\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Harness module")
    parser.add_argument("module_path", help="Module path")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as fatal")
    parser.add_argument("--profile", default="default", help="Profile name")
    args = parser.parse_args()

    result = validate_module(args.module_path, profile=args.profile, strict=args.strict, root_dir=ROOT_DIR)
    _safe_print(result.render_text())
    return result.exit_code(strict=args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
