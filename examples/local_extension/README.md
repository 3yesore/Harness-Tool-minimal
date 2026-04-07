# Project Local Extension Example

This example shows how a project mounts its own extension code without asking `harness_core` to host the runtime.

## What It Demonstrates

- Keep the core harness thin.
- Put project-specific extension code in the project workspace.
- Let the project load and apply its own rules.

## Minimal Layout

```text
examples/local_extension/
  ADAPTER_PROTOCOL.md
  INDEX.md
  SPEC.md
  CHANGELOG.md
  configs/default.json
  src/main.py
  tests/smoke.py
  harness/
    run_harness.py
    extensions/
      entry_consistency.py
      marker_rules.py
  adapters/
    README.md
    protocol.py
    workspace.py
    workflow.py
```

## Key Files

- `harness/extensions/entry_consistency.py`: local entry consistency rule template.
- `harness/extensions/marker_rules.py`: local marker rule template.
- `harness/run_harness.py`: local wrapper that loads and prints the rules.
- `ADAPTER_PROTOCOL.md`: local adapter envelope declaration.
- `adapters/protocol.py`: local adapter protocol shell.
- `adapters/workspace.py` / `adapters/workflow.py`: local adapter samples.

## Reading Order

1. Read `INDEX.md`.
2. Read `SPEC.md`.
3. Read `harness/run_harness.py`.
4. Read `harness/extensions/entry_consistency.py` and `harness/extensions/marker_rules.py`.
5. Keep the wrapper and rules in the project, not in `harness_core`.

## Rule

- `harness_core` defines the contract and guidance.
- The project owns the extension modules.
- The project wrapper loads those modules on its own.
- The core does not mount them for you.
