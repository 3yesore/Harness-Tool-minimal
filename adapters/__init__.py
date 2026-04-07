"""Adapter protocol envelope for Harness Tool external integration."""

from __future__ import annotations

from .protocol import (
    ADAPTER_LIFECYCLE,
    ADAPTER_PROTOCOL_VERSION,
    AdapterContext,
    AdapterResult,
    AdapterSpec,
    describe_adapter_protocol,
)
from .multi_agent import MultiAgentAdapter, build_multi_agent_adapter
from .openharness_bridge import (
    OpenHarnessBridgeAdapter,
    build_openharness_bridge_adapter,
    export_openharness_integration,
)
from .openharness_sdk_binding import (
    OpenHarnessSdkBinding,
    build_openharness_sdk_binding,
    export_openharness_sdk_binding,
)
from .os import OSAdapter, build_os_adapter
from .project_bridge import ProjectBridgeAdapter, build_project_bridge_adapter
from .workflow import WorkflowAdapter, build_workflow_adapter
from .workspace import WorkspaceAdapter, build_workspace_adapter

__all__ = [
    "ADAPTER_LIFECYCLE",
    "ADAPTER_PROTOCOL_VERSION",
    "AdapterContext",
    "AdapterResult",
    "AdapterSpec",
    "MultiAgentAdapter",
    "OpenHarnessBridgeAdapter",
    "OpenHarnessSdkBinding",
    "OSAdapter",
    "ProjectBridgeAdapter",
    "WorkspaceAdapter",
    "WorkflowAdapter",
    "describe_adapter_protocol",
    "build_multi_agent_adapter",
    "build_openharness_bridge_adapter",
    "build_openharness_sdk_binding",
    "build_os_adapter",
    "build_project_bridge_adapter",
    "build_workspace_adapter",
    "build_workflow_adapter",
    "export_openharness_integration",
    "export_openharness_sdk_binding",
]
