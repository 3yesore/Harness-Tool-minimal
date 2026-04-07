"""OpenHarness bridge sample.

This bridge keeps OpenHarness as an external runtime source. It does not host
OpenHarness inside Harness Tool. The bridge only translates a small,
documented set of OpenHarness concepts into the local adapter envelope.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from harness_core import build_module_context, validate_module

from .protocol import AdapterContext, AdapterResult, AdapterSpec

OPENHARNESS_PRIMITIVES = (
    "Agent",
    "Session",
    "Middleware",
    "Subagents",
    "Skills",
    "Providers",
)


def _clean_text(value: str) -> str:
    return " ".join(value.strip().split())


def _read_text_if_exists(path: Path) -> str:
    if not path.exists() or not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _markdown_summary(path: Path, max_lines: int = 3) -> str:
    text = _read_text_if_exists(path)
    if not text:
        return ""
    lines: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or line.startswith("```"):
            continue
        lines.append(_clean_text(line))
        if len(lines) >= max_lines:
            break
    return " ".join(lines)


def _marker_summary(context: Any) -> dict[str, str]:
    return {rule.name: rule.path for rule in context.marker_rules}


def _bullet_lines(items: dict[str, Any]) -> list[str]:
    return [f"- {name}: {value}" for name, value in items.items()]


@dataclass
class OpenHarnessBridgeAdapter:
    """Minimal OpenHarness bridge shell.

    The bridge is intentionally narrow:
    - discover whether an external OpenHarness integration point exists
    - attach a bridge spec owned by the local project
    - adapt a subset of OpenHarness primitives into harness-friendly context
    - execute a shallow bridge pass
    - teardown without owning the external runtime
    """

    spec: AdapterSpec
    workspace_path: Path
    primitives: tuple[str, ...] = OPENHARNESS_PRIMITIVES
    metadata: dict[str, Any] = field(default_factory=dict)

    def discover(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note(f"OpenHarness bridge discovered at {self.workspace_path}")
        return result

    def attach(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note(f"Attached OpenHarness bridge {self.spec.name} v{self.spec.version}")
        return result

    def adapt(self) -> AdapterContext:
        meta = dict(self.metadata)
        meta["openharness_primitives"] = self.primitives
        return AdapterContext(
            spec=self.spec,
            root_path=self.workspace_path,
            workspace_path=self.workspace_path,
            source=self.spec.entrypoint,
            target="openharness",
            metadata=meta,
        )

    def build_context_payload(
        self,
        module_name: str,
        index_summary: str,
        spec_summary: str,
        marker_summary: dict[str, Any] | None = None,
        validation_result: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Build the minimal upstream payload for an OpenHarness agent."""
        return {
            "bridge_version": self.spec.version,
            "source": "harness_tool",
            "target": "openharness",
            "module_name": module_name,
            "index_summary": _clean_text(index_summary),
            "spec_summary": _clean_text(spec_summary),
            "marker_summary": dict(marker_summary or {}),
            "validation_result": dict(validation_result or {}),
            "allowed_primitives": list(self.primitives),
        }

    def build_provider_hints(
        self,
        module_path: str | Path,
        *,
        profile: str = "default",
        strict: bool = False,
    ) -> dict[str, Any]:
        """Build narrow provider hints for an external OpenHarness runtime."""
        context = self.build_openharness_context(
            module_path,
            profile=profile,
            strict=strict,
            include_validation=True,
        )
        return {
            "provider_mode": "external-runtime-owned",
            "recommended_provider_role": "model-and-tool-host",
            "bridge_constraints": [
                "Do not move provider lifecycle into harness_tool.",
                "Treat harness_validate as an external process-backed tool.",
                "Use harness_tool context payload as upstream project context, not as provider state.",
            ],
            "context_payload": context,
        }

    def build_middleware_hints(
        self,
        module_path: str | Path,
        *,
        profile: str = "default",
        strict: bool = False,
    ) -> dict[str, Any]:
        """Build narrow middleware hints for an external OpenHarness runtime."""
        validation = self.run_validate_tool(module_path, profile=profile, strict=strict)
        return {
            "middleware_mode": "external-runtime-owned",
            "recommended_hooks": [
                "preflight_validate",
                "context_injection",
                "postflight_result_normalization",
            ],
            "bridge_constraints": [
                "Run harness_validate before non-trivial file changes.",
                "Inject INDEX/SPEC/marker summaries before task execution.",
                "Normalize downstream output back into summary, notes, warnings, patch_draft, and next_actions.",
            ],
            "validation_snapshot": {
                "status": validation.get("status"),
                "errors": len(validation.get("errors", [])),
                "warnings": len(validation.get("warnings", [])),
            },
        }

    def build_validate_tool_definition(self) -> dict[str, Any]:
        """Return the minimal validate tool definition for an OpenHarness agent."""
        return {
            "name": "harness_validate",
            "description": "Run Harness Tool validation as a preflight contract gate.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "module_path": {"type": "string"},
                    "profile": {"type": "string", "default": "default"},
                    "strict": {"type": "boolean", "default": False},
                },
                "required": ["module_path"],
            },
            "output_schema": {
                "type": "object",
                "properties": {
                    "status": {"type": "string"},
                    "errors": {"type": "array"},
                    "warnings": {"type": "array"},
                    "notes": {"type": "array"},
                    "next_actions": {"type": "array"},
                    "patch_draft": {"type": "array"},
                    "stage_trace": {"type": "array"},
                    "rendered_text": {"type": "string"},
                },
                "required": ["status", "errors", "warnings", "notes", "rendered_text"],
            },
        }

    def run_validate_tool(
        self,
        module_path: str | Path,
        *,
        profile: str = "default",
        strict: bool = False,
    ) -> dict[str, Any]:
        """Execute Harness validation and normalize it as a tool result."""
        result = validate_module(module_path, profile=profile, strict=strict, root_dir=self.workspace_path)
        payload = result.to_dict()
        payload["rendered_text"] = result.render_text()
        payload["strict"] = strict
        payload["tool"] = "harness_validate"
        return payload

    def build_openharness_context(
        self,
        module_path: str | Path,
        *,
        profile: str = "default",
        strict: bool = False,
        include_validation: bool = True,
    ) -> dict[str, Any]:
        """Build an OpenHarness-ready payload from a real Harness module."""
        context = build_module_context(module_path, profile=profile, root_dir=self.workspace_path)
        module_root = context.module_path
        validation_payload = (
            self.run_validate_tool(module_root, profile=profile, strict=strict)
            if include_validation
            else {"status": "skipped"}
        )
        return self.build_context_payload(
            module_name=context.module_name,
            index_summary=_markdown_summary(module_root / "INDEX.md"),
            spec_summary=_markdown_summary(module_root / "SPEC.md"),
            marker_summary=_marker_summary(context),
            validation_result=validation_payload,
        )

    def build_openharness_bundle(
        self,
        module_path: str | Path,
        *,
        profile: str = "default",
        strict: bool = False,
        include_validation: bool = True,
    ) -> dict[str, Any]:
        """Build the minimal bundle an OpenHarness integration can register or inject."""
        return {
            "tool_definition": self.build_validate_tool_definition(),
            "context_payload": self.build_openharness_context(
                module_path,
                profile=profile,
                strict=strict,
                include_validation=include_validation,
            ),
            "bridge": {
                "name": self.spec.name,
                "version": self.spec.version,
                "entrypoint": self.spec.entrypoint,
                "allowed_primitives": list(self.primitives),
            },
        }

    def build_tool_call_example(
        self,
        module_path: str | Path,
        *,
        profile: str = "default",
        strict: bool = False,
    ) -> dict[str, Any]:
        """Build the minimal tool-call payload an OpenHarness agent would send."""
        return {
            "tool": "harness_validate",
            "arguments": {
                "module_path": str(Path(module_path)),
                "profile": profile,
                "strict": strict,
            },
        }

    def build_agent_context_injection(
        self,
        module_path: str | Path,
        *,
        profile: str = "default",
        strict: bool = False,
        include_validation: bool = True,
    ) -> str:
        """Build a plain-text context block for an OpenHarness agent."""
        payload = self.build_openharness_context(
            module_path,
            profile=profile,
            strict=strict,
            include_validation=include_validation,
        )
        marker_lines = _bullet_lines(payload["marker_summary"])
        validation = payload["validation_result"]
        validation_lines = [
            f"- status: {validation.get('status', 'unknown')}",
            f"- errors: {len(validation.get('errors', []))}",
            f"- warnings: {len(validation.get('warnings', []))}",
        ]
        lines = [
            "Harness Tool Context Injection",
            "",
            f"Module: {payload['module_name']}",
            f"Target runtime: {payload['target']}",
            "",
            "Index summary:",
            payload["index_summary"] or "(missing)",
            "",
            "Spec summary:",
            payload["spec_summary"] or "(missing)",
            "",
            "Marker summary:",
            "",
        ]
        lines.extend(marker_lines if marker_lines else ["- none"])
        lines.extend(["", "Validation snapshot:"])
        lines.extend(validation_lines)
        return "\n".join(lines)

    def build_skill_snippet(
        self,
        module_path: str | Path,
        *,
        profile: str = "default",
        strict: bool = False,
        include_validation: bool = True,
    ) -> str:
        """Build a minimal skill-style snippet for OpenHarness context injection."""
        payload = self.build_openharness_context(
            module_path,
            profile=profile,
            strict=strict,
            include_validation=include_validation,
        )
        marker_lines = _bullet_lines(payload["marker_summary"])
        lines = [
            "# Harness Tool Context Skill",
            "",
            "Use this context before changing code in the target module.",
            "",
            "## Module",
            payload["module_name"],
            "",
            "## Index Summary",
            payload["index_summary"] or "(missing)",
            "",
            "## Spec Summary",
            payload["spec_summary"] or "(missing)",
            "",
            "## Marker Summary",
        ]
        lines.extend(marker_lines if marker_lines else ["- none"])
        lines.extend(
            [
                "",
                "## Validation Gate",
                "Run `harness_validate` before applying non-trivial changes.",
                "Treat validation errors as contract blockers.",
            ]
        )
        return "\n".join(lines)

    def normalize_openharness_result(
        self,
        *,
        status: str,
        summary: str,
        notes: list[str] | tuple[str, ...] = (),
        warnings: list[str] | tuple[str, ...] = (),
        patch_draft: list[str] | tuple[str, ...] = (),
        next_actions: list[str] | tuple[str, ...] = (),
    ) -> dict[str, Any]:
        """Normalize a downstream OpenHarness run into a harness-friendly shape."""
        return {
            "status": status,
            "summary": _clean_text(summary),
            "notes": list(notes),
            "warnings": list(warnings),
            "patch_draft": list(patch_draft),
            "next_actions": list(next_actions),
            "source_runtime": "openharness",
        }

    def export_openharness_integration(
        self,
        module_path: str | Path,
        *,
        profile: str = "default",
        strict: bool = False,
        include_validation: bool = True,
    ) -> dict[str, Any]:
        """Export the full narrow bridge surface for a real OpenHarness integration."""
        module_root = Path(module_path)
        bundle = self.build_openharness_bundle(
            module_root,
            profile=profile,
            strict=strict,
            include_validation=include_validation,
        )
        return {
            "bridge": {
                "name": self.spec.name,
                "version": self.spec.version,
                "protocol_version": self.spec.version,
                "entrypoint": self.spec.entrypoint,
                "mode": "bridge-first",
                "host_runtime": False,
                "allowed_primitives": list(self.primitives),
            },
            "module": {
                "path": str(module_root),
                "profile": profile,
                "strict": strict,
            },
            "registration": {
                "tool_definition": bundle["tool_definition"],
                "context_payload": bundle["context_payload"],
                "provider_hints": self.build_provider_hints(
                    module_root,
                    profile=profile,
                    strict=strict,
                ),
                "middleware_hints": self.build_middleware_hints(
                    module_root,
                    profile=profile,
                    strict=strict,
                ),
                "agent_context_injection": self.build_agent_context_injection(
                    module_root,
                    profile=profile,
                    strict=strict,
                    include_validation=include_validation,
                ),
                "skill_snippet": self.build_skill_snippet(
                    module_root,
                    profile=profile,
                    strict=strict,
                    include_validation=include_validation,
                ),
            },
            "examples": {
                "validate_tool_call": self.build_tool_call_example(
                    module_root,
                    profile=profile,
                    strict=strict,
                ),
            },
            "references": {
                "bridge_spec": "OPENHARNESS_BRIDGE.md",
                "open_items": "docs/OPENHARNESS_BRIDGE_OPEN_ITEMS.md",
                "work_index": "docs/OPENHARNESS_BRIDGE_INDEX.md",
            },
        }

    def execute(self) -> AdapterResult:
        context = self.adapt()
        payload = self.build_context_payload(
            module_name=self.spec.name,
            index_summary="Use INDEX.md as the first repository entry.",
            spec_summary="Use SPEC.md as the contract reference before code changes.",
            marker_summary={"bridge": "openharness", "shell": True},
            validation_result={"status": "pending"},
        )
        result = AdapterResult(
            status="success",
            adapted_context={
                "workspace_path": str(context.workspace_path),
                "scope": context.spec.scope,
                "target": context.target,
                "openharness_primitives": list(self.primitives),
                "shell": True,
                "context_payload": payload,
            },
            capability_report=self.spec.capabilities,
        )
        result.add_note("This bridge only maps OpenHarness concepts into the local envelope.")
        result.add_note("Keep OpenHarness runtime ownership outside harness_core.")
        return result

    def teardown(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note("OpenHarness bridge teardown complete")
        return result


def build_openharness_bridge_adapter(
    workspace_path: str | Path,
    name: str = "openharness_bridge",
) -> OpenHarnessBridgeAdapter:
    path = Path(workspace_path)
    spec = AdapterSpec(
        name=name,
        version="v1.0.1 beta",
        type="bridge",
        scope="project",
        entrypoint="adapters/openharness_bridge.py",
        capabilities=("discover", "attach", "adapt", "execute", "teardown"),
        notes=(
            "Bridge OpenHarness as an external capability source.",
            "Do not turn Harness Tool into an OpenHarness host runtime.",
        ),
    )
    return OpenHarnessBridgeAdapter(spec=spec, workspace_path=path)


def export_openharness_integration(
    workspace_path: str | Path,
    module_path: str | Path,
    *,
    profile: str = "default",
    strict: bool = False,
    include_validation: bool = True,
) -> dict[str, Any]:
    """Convenience helper for exporting the full OpenHarness bridge surface."""
    adapter = build_openharness_bridge_adapter(workspace_path)
    return adapter.export_openharness_integration(
        module_path,
        profile=profile,
        strict=strict,
        include_validation=include_validation,
    )
