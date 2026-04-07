from __future__ import annotations


def run() -> dict[str, str]:
    return {
        "status": "success",
        "message": "local extension is ready",
    }


def main() -> int:
    result = run()
    print(result["message"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
