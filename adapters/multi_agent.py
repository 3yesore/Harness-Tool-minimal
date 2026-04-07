"""Multi-agent adapter sample template.

This is a minimal shell for projects that want to coordinate multiple agents
without making harness_core responsible for orchestration internals.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .protocol import AdapterContext, AdapterResult, AdapterSpec


@dataclass
class MultiAgentAdapter:
    """Minimal multi-agent adapter shell.

    The template only demonstrates the envelope:
    - discover a coordination target
    - attach an adapter spec
    - adapt agent context into a normalized shape
    - execute project-owned coordination logic
    - teardown cleanly
    """

    spec: AdapterSpec
    workspace_path: Path
    agent_names: tuple[str, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)

    def discover(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note(f"Multi-agent adapter shell discovered at {self.workspace_path}")
        return result

    def attach(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note(f"Attached multi-agent adapter shell {self.spec.name} v{self.spec.version}")
        return result

    def adapt(self) -> AdapterContext:
        meta = dict(self.metadata)
        meta["agent_names"] = self.agent_names
        return AdapterContext(
            spec=self.spec,
            root_path=self.workspace_path,
            workspace_path=self.workspace_path,
            source=self.spec.entrypoint,
            target="multi_agent",
            metadata=meta,
        )

    def execute(self) -> AdapterResult:
        context = self.adapt()
        result = AdapterResult(
            status="success",
            adapted_context={
                "workspace_path": str(context.workspace_path),
                "agent_names": list(self.agent_names),
                "scope": context.spec.scope,
                "shell": True,
            },
            capability_report=self.spec.capabilities,
        )
        result.add_note("Multi-agent adapter template only defines the envelope. Keep orchestration project-owned.")
        return result

    def teardown(self) -> AdapterResult:
        result = AdapterResult(status="success")
        result.add_note("Multi-agent adapter shell teardown complete")
        return result


def build_multi_agent_adapter(
    workspace_path: str | Path,
    name: str = "multi_agent",
    agent_names: tuple[str, ...] = (),
) -> MultiAgentAdapter:
    path = Path(workspace_path)
    spec = AdapterSpec(
        name=name,
        version="v1.0.1 beta",
        type="multi_agent",
        scope="workflow",
        entrypoint="adapters/multi_agent.py",
        capabilities=("discover", "attach", "adapt", "execute", "teardown"),
    )
    return MultiAgentAdapter(spec=spec, workspace_path=path, agent_names=agent_names)
