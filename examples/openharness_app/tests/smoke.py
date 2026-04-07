#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    executable = shutil.which(args[0]) or shutil.which(f"{args[0]}.cmd") or args[0]
    return subprocess.run(
        [executable, *args[1:]],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    if not (ROOT / "node_modules").exists():
        print("[SKIP] openharness_app npm dependencies are not installed; skipping npm build/smoke.")
        return 0

    build = run(["npm", "run", "build"])
    if build.returncode != 0:
        print(build.stdout)
        print(build.stderr, file=sys.stderr)
        raise SystemExit(build.returncode)

    smoke = run(["npm", "run", "smoke"])
    if smoke.returncode != 0:
        print(smoke.stdout)
        print(smoke.stderr, file=sys.stderr)
        raise SystemExit(smoke.returncode)

    print("[PASS] openharness_app smoke test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
