# OpenHarness Bridge Index

This index is the work-order map for the OpenHarness bridge line.

## Stable Inputs
- `OPENHARNESS_BRIDGE.md`
- `adapters/openharness_bridge.py`
- `ADAPTER_PROTOCOL.md`
- `CORE_PROTOCOL.md`
- `EXTENSION_PROTOCOL.md`
- `harness_core/`
- `tools/validate_module.py`
- `examples/openharness_app/`

## Still Open
- `docs/OPENHARNESS_BRIDGE_OPEN_ITEMS.md`
- real OpenHarness package binding
- provider mapping
- middleware mapping
- real skill / `AGENTS.md` registration path
- bridge-specific validation matrix

## Recommended Order
1. Keep the bridge spec stable.
2. Keep the bridge shell narrow.
3. Keep the exported integration surface stable.
4. Add one real OpenHarness integration path.
5. Validate the bridge without widening `core`.
6. Only then decide whether more bridge coverage is justified.
