"""External project bridge adapter sample.

This module is a minimal shell for wrapping an external open-source project
without moving project-specific runtime or integration logic into
`harness_core`.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .protocol import AdapterContext, AdapterResult, AdapterSpec


@dataclass
class ProjectBridgeAdapter:
    """Minimal external project bridge adapter shell.

    The sample only demonstrates the envelope:
    - discover the external project boundary
    - attach a thin adapter spec
    - adapt project metadata into a normalized context
    - execute project-owned bridge hooks
    - teardown cleanly
    """

    spec: AdapterSpec
    workspace_path: Path
    project_name: str = "external-project"
    metadata: dict[str, Any] = field(default_factory=dict)

    def discover(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note(f"Project bridge adapter discovered at {self.workspace_path}")
        return result

    def attach(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note(f"Attached project bridge adapter {self.spec.name} v{self.spec.version}")
        return result

    def adapt(self) -> AdapterContext:
        meta = dict(self.metadata)
        meta["project_name"] = self.project_name
        return AdapterContext(
            spec=self.spec,
            root_path=self.workspace_path,
            workspace_path=self.workspace_path,
            source=self.spec.entrypoint,
            target="project_bridge",
            metadata=meta,
        )

    def execute(self) -> AdapterResult:
        context = self.adapt()
        result = AdapterResult(
            status="success",
            adapted_context={
                "workspace_path": str(context.workspace_path),
                "project_name": self.project_name,
                "scope": context.spec.scope,
                "shell": True,
            },
            capability_report=self.spec.capabilities,
        )
        result.add_note(
            "Project bridge adapter is a sample envelope. Keep external project hooks project-owned."
        )
        return result

    def teardown(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note("Project bridge adapter teardown complete")
        return result


def build_project_bridge_adapter(
    workspace_path: str | Path,
    name: str = "project_bridge",
    project_name: str = "external-project",
) -> ProjectBridgeAdapter:
    path = Path(workspace_path)
    spec = AdapterSpec(
        name=name,
        version="v1.0.1 beta",
        type="project_bridge",
        scope="project",
        entrypoint="adapters/project_bridge.py",
        capabilities=("discover", "attach", "adapt", "execute", "teardown"),
    )
    return ProjectBridgeAdapter(spec=spec, workspace_path=path, project_name=project_name)
