# OpenHarness Provider / Middleware Index

This index is the work-order map for provider and middleware bridge handling.

## Stable Inputs
- `OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md`
- `OPENHARNESS_BRIDGE.md`
- `OPENHARNESS_SDK_BINDING.md`
- `adapters/openharness_bridge.py`
- `adapters/openharness_sdk_binding.py`
- `docs/OPENHARNESS_EXTERNAL_VERIFY.md`

## Still Open
- `docs/OPENHARNESS_PROVIDER_MIDDLEWARE_OPEN_ITEMS.md`
- live provider registration wiring
- live middleware registration wiring
- non-process transport
- session / conversation validation

## Recommended Order
1. Keep provider and middleware hints bridge-only.
2. Keep the contract stable.
3. Validate hint export in a real external OpenHarness app.
4. Only then add runtime-side registration examples.
