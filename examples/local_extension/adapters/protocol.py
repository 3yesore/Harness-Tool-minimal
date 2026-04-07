"""Local adapter protocol shell for the local_extension example."""

from __future__ import annotations

from adapters import (
    ADAPTER_LIFECYCLE,
    ADAPTER_PROTOCOL_VERSION,
    AdapterContext,
    AdapterResult,
    AdapterSpec,
    describe_adapter_protocol,
)

__all__ = [
    "ADAPTER_LIFECYCLE",
    "ADAPTER_PROTOCOL_VERSION",
    "AdapterContext",
    "AdapterResult",
    "AdapterSpec",
    "describe_adapter_protocol",
]
