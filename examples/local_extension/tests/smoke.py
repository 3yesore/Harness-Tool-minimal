#!/usr/bin/env python3
from __future__ import annotations

import io
import sys
from pathlib import Path


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from main import run  # noqa: E402


def main() -> int:
    result = run()
    assert result["status"] == "success"
    print("[PASS] local_extension smoke test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
