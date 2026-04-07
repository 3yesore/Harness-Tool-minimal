# OpenHarness External Verify

## Result
The current OpenHarness bridge and SDK binding were verified in a repo-external
OpenHarness app directory:

- external path: `C:/Users/Y2516/Desktop/openharness_app_external_verify`
- dependency install: passed
- TypeScript build: passed
- smoke run: passed

## Verified Scope
- `@openharness/core@0.6.0` `Agent` instantiation
- `Agent.run(...)` dry-run with a local mock model and no real model request
- process transport call into `scripts/openharness_validate_transport.py`
- SDK binding export loading from the current `harness_tool` repo
- provider and middleware hints exported as narrow bridge metadata
- runtime-side registration example consumed in `src/runtime-registration.ts`
- external app template split into:
  - `src/binding.ts`
  - `src/transport.ts`
  - `src/runtime-registration.ts`
  - `src/mock-model.ts`
  - `src/smoke.ts`
  - `README.md`

## Not Verified
- real model call
- provider registration wiring
- middleware registration wiring
- session / conversation execution
- non-process transport

## Commands Used
```bash
npm install
npm run build
npm run smoke
```

## Why This Matters
This proves the current bridge is not only repo-local. A separate OpenHarness
app can consume the binding export and call the validate transport without
widening `core`.
