#!/usr/bin/env python3
"""Initialize a new Harness module."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from harness_core import init_module  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a new Harness module")
    parser.add_argument("module_name", help="Module name")
    parser.add_argument("--path", default="modules", help="Output directory")
    parser.add_argument("--profile", default="default", help="Profile name")
    args = parser.parse_args()

    plan = init_module(args.module_name, output_dir=args.path, profile=args.profile, root_dir=ROOT_DIR)
    print(f"[OK] initialized module: {plan.module_path}")
    print("[OK] created files:")
    for relpath in sorted(plan.create_files):
        print(f"  - {relpath}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
