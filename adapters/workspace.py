"""Workspace adapter sample for external integration experiments.

This module is intentionally small. It shows how a project can own its own
adapter wrapper without pushing adapter runtime concerns into harness_core.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .protocol import AdapterContext, AdapterResult, AdapterSpec


@dataclass
class WorkspaceAdapter:
    """Minimal workspace adapter sample.

    The sample only demonstrates the envelope:
    - discover external workspace information
    - adapt it into a normalized context
    - report capabilities and warnings
    """

    spec: AdapterSpec
    workspace_path: Path
    metadata: dict[str, Any] = field(default_factory=dict)

    def discover(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note(f"Workspace discovered at {self.workspace_path}")
        return result

    def attach(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note(f"Attached adapter {self.spec.name} v{self.spec.version}")
        return result

    def adapt(self) -> AdapterContext:
        return AdapterContext(
            spec=self.spec,
            root_path=self.workspace_path,
            workspace_path=self.workspace_path,
            source=self.spec.entrypoint,
            target="harness_core",
            metadata=dict(self.metadata),
        )

    def execute(self) -> AdapterResult:
        context = self.adapt()
        result = AdapterResult(
            status="success",
            adapted_context={
                "workspace_path": str(context.workspace_path),
                "entrypoint": context.spec.entrypoint,
                "scope": context.spec.scope,
            },
            capability_report=self.spec.capabilities,
        )
        result.add_note("This is a sample adapter; hook your own OS / workflow behavior here.")
        return result

    def teardown(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note("Workspace adapter teardown complete")
        return result


def build_workspace_adapter(workspace_path: str | Path, name: str = "workspace") -> WorkspaceAdapter:
    path = Path(workspace_path)
    spec = AdapterSpec(
        name=name,
        version="v1.0.1 beta",
        type="workspace",
        scope="workspace",
        entrypoint="adapters/workspace.py",
        capabilities=("discover", "attach", "adapt", "execute", "teardown"),
    )
    return WorkspaceAdapter(spec=spec, workspace_path=path)
