"""OS adapter sample template.

This is a minimal shell for projects that want to translate operating-system
capabilities into harness-friendly adapter inputs without moving runtime logic
into harness_core.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .protocol import AdapterContext, AdapterResult, AdapterSpec


@dataclass
class OSAdapter:
    """Minimal OS adapter shell.

    The template only demonstrates the envelope:
    - discover an OS/workspace boundary
    - attach a thin adapter spec
    - adapt the environment into a normalized context
    - execute project-owned OS integration hooks
    - teardown cleanly
    """

    spec: AdapterSpec
    workspace_path: Path
    metadata: dict[str, Any] = field(default_factory=dict)

    def discover(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note(f"OS adapter shell discovered at {self.workspace_path}")
        return result

    def attach(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note(f"Attached OS adapter shell {self.spec.name} v{self.spec.version}")
        return result

    def adapt(self) -> AdapterContext:
        return AdapterContext(
            spec=self.spec,
            root_path=self.workspace_path,
            workspace_path=self.workspace_path,
            source=self.spec.entrypoint,
            target="os",
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
                "shell": True,
            },
            capability_report=self.spec.capabilities,
        )
        result.add_note("OS adapter template only defines the envelope. Keep OS hooks project-owned.")
        return result

    def teardown(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note("OS adapter shell teardown complete")
        return result


def build_os_adapter(workspace_path: str | Path, name: str = "os") -> OSAdapter:
    path = Path(workspace_path)
    spec = AdapterSpec(
        name=name,
        version="v1.0.1 beta",
        type="os",
        scope="workspace",
        entrypoint="adapters/os.py",
        capabilities=("discover", "attach", "adapt", "execute", "teardown"),
    )
    return OSAdapter(spec=spec, workspace_path=path)
