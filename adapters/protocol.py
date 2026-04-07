"""Minimal adapter protocol envelope for external integration points."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ADAPTER_PROTOCOL_VERSION = "v1.0.1 beta"
ADAPTER_LIFECYCLE = (
    "discover",
    "attach",
    "adapt",
    "execute",
    "teardown",
)
ADAPTER_BOUNDARIES = {
    "version": ADAPTER_PROTOCOL_VERSION,
    "role": "Translate external runtimes into standard Harness Tool inputs.",
    "hard": "Envelope, lifecycle, capability declaration, and compatibility are frozen.",
    "soft": "Internal implementation details may vary by project or adapter type.",
    "boundary": "Adapter translates; core validates; extension customizes.",
}


@dataclass(frozen=True)
class AdapterSpec:
    name: str
    version: str
    type: str
    scope: str
    entrypoint: str
    capabilities: tuple[str, ...] = ()
    protocol_version: str = ADAPTER_PROTOCOL_VERSION
    required_core_version: str = "v1.0.1 beta"
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class AdapterContext:
    spec: AdapterSpec
    root_path: Path
    workspace_path: Path
    source: str
    target: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class AdapterResult:
    status: str = "success"
    adapted_context: dict[str, Any] = field(default_factory=dict)
    capability_report: tuple[str, ...] = ()
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def add_warning(self, message: str) -> None:
        self.warnings.append(message)

    def add_error(self, message: str) -> None:
        self.errors.append(message)

    def add_note(self, message: str) -> None:
        self.notes.append(message)

    def exit_code(self) -> int:
        return 1 if self.errors else 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "adapted_context": dict(self.adapted_context),
            "capability_report": list(self.capability_report),
            "warnings": list(self.warnings),
            "errors": list(self.errors),
            "notes": list(self.notes),
        }


def describe_adapter_protocol() -> str:
    lines = [
        f"Adapter protocol version: {ADAPTER_PROTOCOL_VERSION}",
        "Lifecycle: " + " -> ".join(ADAPTER_LIFECYCLE),
    ]
    for name, description in ADAPTER_BOUNDARIES.items():
        lines.append(f"- {name}: {description}")
    return "\n".join(lines)
