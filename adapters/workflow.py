"""Workflow adapter sample for staged external coordination experiments.

This sample stays intentionally small. It demonstrates how a project can wrap
a staged workflow without turning the adapter layer into a runtime platform.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .protocol import AdapterContext, AdapterResult, AdapterSpec


@dataclass
class WorkflowAdapter:
    """Minimal workflow adapter sample.

    The adapter demonstrates a staged workflow:
    - discover the coordination target
    - attach a local plan
    - adapt the local state
    - execute a shallow workflow
    - teardown cleanly
    """

    spec: AdapterSpec
    workspace_path: Path
    stages: tuple[str, ...] = ("discover", "attach", "adapt", "execute", "teardown")
    metadata: dict[str, Any] = field(default_factory=dict)

    def discover(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note(f"Workflow target discovered at {self.workspace_path}")
        return result

    def attach(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note(f"Workflow adapter attached: {self.spec.name}")
        return result

    def adapt(self) -> AdapterContext:
        meta = dict(self.metadata)
        meta["stages"] = self.stages
        return AdapterContext(
            spec=self.spec,
            root_path=self.workspace_path,
            workspace_path=self.workspace_path,
            source=self.spec.entrypoint,
            target="workflow",
            metadata=meta,
        )

    def execute(self) -> AdapterResult:
        context = self.adapt()
        result = AdapterResult(
            status="success",
            adapted_context={
                "workspace_path": str(context.workspace_path),
                "stages": list(self.stages),
                "scope": context.spec.scope,
            },
            capability_report=self.spec.capabilities,
        )
        result.add_note("This adapter is a sample workflow envelope, not a runtime platform.")
        return result

    def teardown(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note("Workflow adapter teardown complete")
        return result


def build_workflow_adapter(workspace_path: str | Path, name: str = "workflow") -> WorkflowAdapter:
    path = Path(workspace_path)
    spec = AdapterSpec(
        name=name,
        version="v1.0.1 beta",
        type="workflow",
        scope="workflow",
        entrypoint="adapters/workflow.py",
        capabilities=("discover", "attach", "adapt", "execute", "teardown"),
    )
    return WorkflowAdapter(spec=spec, workspace_path=path)
