"""Local adapter sample package for the local_extension example."""

from __future__ import annotations

from adapters import (
    ADAPTER_LIFECYCLE,
    ADAPTER_PROTOCOL_VERSION,
    AdapterContext,
    AdapterResult,
    AdapterSpec,
    WorkspaceAdapter,
    WorkflowAdapter,
    build_workspace_adapter,
    build_workflow_adapter,
    describe_adapter_protocol,
)

__all__ = [
    "ADAPTER_LIFECYCLE",
    "ADAPTER_PROTOCOL_VERSION",
    "AdapterContext",
    "AdapterResult",
    "AdapterSpec",
    "WorkspaceAdapter",
    "WorkflowAdapter",
    "build_workspace_adapter",
    "build_workflow_adapter",
    "describe_adapter_protocol",
]
