"""OpenHarness process transport for Harness Tool validation.

This script is the narrow process boundary between an OpenHarness runtime and
the local Harness Tool bridge. It keeps runtime ownership outside the repo and
returns normalized JSON only.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from adapters import build_openharness_bridge_adapter  # noqa: E402


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run harness_validate for an OpenHarness runtime.")
    parser.add_argument("--workspace-path", default=".", help="Harness Tool workspace root.")
    parser.add_argument("--module-path", help="Module path relative to the workspace root.")
    parser.add_argument("--profile", default="default", help="Harness profile name.")
    parser.add_argument("--strict", action="store_true", help="Enable strict validation mode.")
    parser.add_argument(
        "--stdin-json",
        action="store_true",
        help="Read transport input from stdin as JSON instead of CLI flags.",
    )
    return parser


def _load_payload(args: argparse.Namespace) -> dict[str, Any]:
    if not args.stdin_json:
        if not args.module_path:
            raise ValueError("--module-path is required unless --stdin-json is used.")
        return {
            "workspace_path": args.workspace_path,
            "module_path": args.module_path,
            "profile": args.profile,
            "strict": args.strict,
        }
    raw = sys.stdin.read().strip()
    if not raw:
        raise ValueError("stdin-json mode requires a JSON payload on stdin.")
    payload = json.loads(raw)
    if "module_path" not in payload:
        raise ValueError("stdin-json payload must include module_path.")
    return {
        "workspace_path": payload.get("workspace_path", "."),
        "module_path": payload["module_path"],
        "profile": payload.get("profile", "default"),
        "strict": bool(payload.get("strict", False)),
    }


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()
    try:
        payload = _load_payload(args)
        adapter = build_openharness_bridge_adapter(payload["workspace_path"])
        result = adapter.run_validate_tool(
            payload["module_path"],
            profile=payload["profile"],
            strict=payload["strict"],
        )
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 0
    except Exception as exc:  # pragma: no cover - transport shell fallback
        error_payload = {
            "tool": "harness_validate",
            "status": "error",
            "errors": [str(exc)],
            "warnings": [],
            "notes": ["OpenHarness validate transport failed before bridge execution."],
            "next_actions": ["Inspect the transport arguments and local workspace path."],
            "patch_draft": [],
            "stage_trace": [],
            "rendered_text": f"transport error: {exc}",
        }
        json.dump(error_payload, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
