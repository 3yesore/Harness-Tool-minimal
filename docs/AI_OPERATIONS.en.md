# Harness AI Operations Guide v1.0.1 beta

This guide describes how to work on a module in this repository without losing the Harness contract.

## Workflow

1. Read the target module `INDEX.md` first.
2. Read the target module `SPEC.md` next.
3. Read only the files needed for the task.
4. Make the smallest change that solves the problem.
5. Run the smoke test.
6. Run the validator.
7. Update `CHANGELOG.md` when behavior changes.

## Current Commands

```bash
python tools/init_module.py my_module
python tools/apply_harness.py path/to/module
python tools/apply_harness.py path/to/module --profile python-service
python tools/validate_module.py path/to/module
python tools/validate_module.py path/to/module --strict
python tools/validate_module.py path/to/module --strict --profile python-service
```

## What To Avoid

- do not read the whole codebase before checking the module index
- do not change the module contract without updating `SPEC.md`
- do not change key module files without updating `INDEX.md`
- do not skip the smoke test
- do not turn the kernel into a thick framework

## If A Module Is Missing Harness Files

Use `apply_harness.py` to add the missing skeleton files, then edit the generated docs to match the real module behavior.

## `1.0.1 beta` Status

The repository is now frozen as a thin, contract-driven beta baseline. Future changes must stay within the four-layer model:

- `kernel`
- `contract`
- `extension`
- `override`

## OpenHarness Boundary

- OpenHarness integration remains bridge-side, not core-side.
- Treat bridge and binding files as external integration artifacts.
- Do not move provider, middleware, session, or runtime ownership into `harness_core`.
