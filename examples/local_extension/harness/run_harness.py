from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def load_local_module(module_path: Path):
    """Load a project-owned extension module from a local file path.

    The project wrapper decides where to load from and what to do with the
    resulting rules. `harness_core` stays out of the mounting path.
    """
    spec = importlib.util.spec_from_file_location(
        module_path.stem,
        module_path,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载本地扩展模块: {module_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    # Real projects usually read these paths from project config.
    # The example keeps them explicit so the mounting pattern stays obvious.
    entry_rule_module = load_local_module(BASE_DIR / "extensions" / "entry_consistency.py")
    marker_rule_module = load_local_module(BASE_DIR / "extensions" / "marker_rules.py")

    # The project wrapper can inspect, log, or forward these rule objects into
    # its own validation workflow.
    entry_rule = entry_rule_module.build_rules()
    marker_rules = marker_rule_module.build_rules()

    print("[LOCAL] entry_consistency")
    print(entry_rule.describe())
    print()
    print("[LOCAL] marker_rules")
    print(marker_rules.describe())


if __name__ == "__main__":
    # Keep the local wrapper entry point thin and explicit.
    main()
