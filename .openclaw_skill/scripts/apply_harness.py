#!/usr/bin/env python3
"""Apply Harness scaffold files from the skill bundle."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from harness_core import apply_harness  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply Harness scaffold files")
    parser.add_argument("module_path", help="Module path")
    parser.add_argument("--profile", default="default", help="Profile name")
    args = parser.parse_args()

    plan = apply_harness(args.module_path, profile=args.profile, root_dir=ROOT_DIR)
    print(f"[OK] applied harness scaffold: {plan.module_path}")
    if plan.create_files:
        print("[OK] created files:")
        for relpath in sorted(plan.create_files):
            print(f"  - {relpath}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
