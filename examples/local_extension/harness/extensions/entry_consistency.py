from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class EntryConsistencyRule:
    """Project-local entry consistency rule.

    This is a template for a real project-owned rule module.
    The project can replace the defaults with its own entry layout,
    while keeping the contract readable for humans and AI.
    """

    # Rule identity and enforcement level are intentionally explicit.
    name: str = "entry_consistency"
    mode: str = "soft"

    # The three paths below describe the same entry from three angles:
    # - INDEX.md entry_file: what the module documents as its entry
    # - SPEC.md call_entry: what the interface contract points to
    # - actual_entry_file: what the project wrapper really executes
    index_entry_file: str = "src/main.py"
    spec_call_entry: str = "src/main.py"
    actual_entry_file: str = "src/main.py"

    def describe(self) -> dict[str, str]:
        """Return a plain dict so the project wrapper can print or log it."""
        return {
            "name": self.name,
            "mode": self.mode,
            "index_entry_file": self.index_entry_file,
            "spec_call_entry": self.spec_call_entry,
            "actual_entry_file": self.actual_entry_file,
        }


def build_rules() -> EntryConsistencyRule:
    # Real projects usually replace this with project-specific defaults,
    # but keeping a single constructor makes the example easy to read.
    return EntryConsistencyRule()
