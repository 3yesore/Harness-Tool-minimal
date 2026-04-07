# OpenHarness Provider / Middleware Open Items

## Still Open
- live provider registration wiring in a real OpenHarness app
- live middleware registration wiring in a real OpenHarness app
- non-process transport
- session / conversation validation
- provider-specific capability narrowing
- middleware-specific ordering tests

## Still Intentionally Out Of Core
- provider lifecycle ownership
- middleware implementation ownership
- session persistence wiring
- conversation runtime wiring
- UI streaming wiring

## Current Rule
Keep provider and middleware handling as bridge metadata until a real external
OpenHarness integration proves a narrower executable contract is necessary.
