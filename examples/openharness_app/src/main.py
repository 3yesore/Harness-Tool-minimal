#!/usr/bin/env python3
from __future__ import annotations

import json


def main() -> int:
    payload = {
        "status": "success",
        "message": "Use `npm run start` to run the TypeScript OpenHarness example.",
        "runtime_entry": "src/main.ts",
    }
    print(json.dumps(payload, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
