# Adapter Layer

This folder is the thin, optional adapter layer for `harness_tool`.

## What it is
- A protocol envelope for external integration
- A place to translate OS / workflow / project differences into standard Harness inputs
- A future home for adapter samples and adapter-specific wrappers

## What it is not
- Not a second core
- Not a plugin runtime
- Not a thick platform
- Not a replacement for `harness_core`

## Current status
- Protocol-first
- Runtime-light
- Extension-friendly

## Entry points
- `adapters.describe_adapter_protocol()`
- `ADAPTER_PROTOCOL.md`
- `CORE_PROTOCOL.md`
- `EXTENSION_PROTOCOL.md`
- `SAMPLES.md`
- `adapters/os.py`
- `adapters/multi_agent.py`
- `adapters/openharness_bridge.py`
- `adapters/project_bridge.py`
- `adapters/workspace.py`
- `adapters/sample_usage.md`
- `adapters/workflow.py`
- `adapters/openharness_sdk_binding.py`
- `adapters/openharness_sdk_binding.sample.ts`
- `scripts/openharness_validate_transport.py`

## Open items kept on purpose
- OS / multi-agent / external project adapters are not fully built yet
- OpenHarness is treated as an external bridge target, not a hosted runtime
- Only one workspace adapter sample exists
- Workflow adapter sample is intentionally small
- Adapter validation is still minimal until the need becomes real

## OpenHarness Bridge
- `OPENHARNESS_BRIDGE.md`
- `OPENHARNESS_SDK_BINDING.md`
- `OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md`
- `docs/OPENHARNESS_BRIDGE_OPEN_ITEMS.md`
- `docs/OPENHARNESS_BRIDGE_INDEX.md`
- `docs/OPENHARNESS_SDK_BINDING_OPEN_ITEMS.md`
- `docs/OPENHARNESS_SDK_BINDING_INDEX.md`
