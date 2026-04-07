from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class MarkerRuleSet:
    """Project-local marker rule set.

    This template shows how a project can keep its own critical paths,
    key state variables, and high-risk couplings outside harness_core.
    """

    # Keep a stable name so the wrapper can print or select this rule set.
    name: str = "marker_rules"

    # Critical paths are the files the project wants AI and humans to inspect first.
    critical_paths: list[str] = field(default_factory=lambda: [
        "src/main.py",
        "configs/default.json",
        "tests/smoke.py",
    ])

    # Critical variables are the state values that should be easy to recover.
    critical_variables: list[str] = field(default_factory=lambda: [
        "module_name",
        "entry_file",
        "config_file",
        "test_file",
    ])

    # Critical couplings are the relationships that tend to break during refactors.
    critical_couplings: list[str] = field(default_factory=lambda: [
        "index_spec_alignment",
        "init_apply_validate_shared_core",
    ])

    def describe(self) -> dict[str, list[str] | str]:
        """Expose a plain summary for a local wrapper or debug print."""
        return {
            "name": self.name,
            "critical_paths": list(self.critical_paths),
            "critical_variables": list(self.critical_variables),
            "critical_couplings": list(self.critical_couplings),
        }


def build_rules() -> MarkerRuleSet:
    # Replace the defaults in the project when the real layout becomes known.
    return MarkerRuleSet()
