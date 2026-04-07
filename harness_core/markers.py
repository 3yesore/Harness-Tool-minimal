"""Marker registry helpers for the frozen Harness protocol."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


CORE_MARKER_KEYS = (
    "entry_file",
    "call_path",
    "call_entry",
    "smoke_test",
    "config",
    "marker_source",
)

DEFAULT_REQUIRED_MARKER_KEYS = (
    "entry_file",
    "call_path",
    "call_entry",
)

DEFAULT_RECOMMENDED_MARKER_KEYS = (
    "smoke_test",
    "config",
    "marker_source",
)


@dataclass(frozen=True)
class MarkerRule:
    name: str
    path: str
    role: str
    required: bool = True

    def resolved(self, root: Path) -> Path:
        return root / self.path

    def exists(self, root: Path) -> bool:
        return self.resolved(root).exists()

    def as_line(self) -> str:
        level = "required" if self.required else "recommended"
        return f"- `{self.name}`: `{self.path}` ({self.role}, {level})"


def _normalize_relpath(value: str | Path) -> str:
    return Path(str(value).replace("\\", "/")).as_posix().lstrip("./")


def build_marker_registry(
    *,
    entry_file: str | Path,
    call_path: str | Path,
    call_entry: str | Path,
    smoke_test: str | Path = "tests/smoke.py",
    config_file: str | Path = "configs/default.json",
    marker_source: str | Path | None = None,
) -> tuple[MarkerRule, ...]:
    rules = [
        MarkerRule("entry_file", _normalize_relpath(entry_file), "module entry"),
        MarkerRule("call_path", _normalize_relpath(call_path), "call site"),
        MarkerRule("call_entry", _normalize_relpath(call_entry), "actual entry"),
        MarkerRule("smoke_test", _normalize_relpath(smoke_test), "smoke test", required=False),
        MarkerRule("config", _normalize_relpath(config_file), "default config", required=False),
    ]
    if marker_source is not None:
        rules.append(
            MarkerRule(
                "marker_source",
                _normalize_relpath(marker_source),
                "local marker rules",
                required=False,
            )
        )
    return tuple(rules)


def render_marker_section(marker_rules: Iterable[MarkerRule]) -> str:
    lines = ["## 关键标记"]
    for rule in marker_rules:
        lines.append(rule.as_line())
    return "\n".join(lines)


def describe_marker_registry(marker_rules: Iterable[MarkerRule] | None = None) -> str:
    rules = tuple(marker_rules or ())
    if not rules:
        return "Marker registry: entry_file, call_path, call_entry, smoke_test, config, marker_source."
    return "\n".join(rule.as_line() for rule in rules)
