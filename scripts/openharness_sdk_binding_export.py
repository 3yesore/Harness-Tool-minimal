"""Export OpenHarness SDK binding data as JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from adapters import export_openharness_sdk_binding  # noqa: E402


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Export OpenHarness SDK binding payload.")
    parser.add_argument("--workspace-path", default=".", help="Harness Tool workspace root.")
    parser.add_argument("--module-path", required=True, help="Module path relative to workspace root.")
    parser.add_argument("--profile", default="default", help="Harness profile name.")
    parser.add_argument("--strict", action="store_true", help="Enable strict validation mode.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    payload = export_openharness_sdk_binding(
        args.workspace_path,
        args.module_path,
        profile=args.profile,
        strict=args.strict,
    )
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
