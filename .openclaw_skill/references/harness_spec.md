# Harness Specification v1.0.1 beta

## What Harness Means Here

Harness is a module development and maintenance contract. It is not a full framework or package manager. The goal is to keep the important context in a few files so that a human or AI can take over quickly.

This repository focuses on:

- a clear `INDEX.md`
- a clear `SPEC.md`
- a runnable smoke test
- lightweight automation
- low handoff cost

## Frozen Protocol

The current beta baseline freezes the core around four primitives:

- `ModuleContext`
- `ContractRules`
- `ValidationResult`
- `ScaffoldPlan`

The workflow stages are:

- `Discovery`
- `Contract`
- `Validate`
- `Suggest`

## Core Principles

### 1. Index First

- Every maintained module should have an `INDEX.md`
- `INDEX.md` should explain responsibilities, key files, dependencies, and the validation entry point
- AI should read the index before scanning code

### 2. Contract Driven

- `SPEC.md` should define inputs, outputs, configuration, call entry, and error handling
- If the interface changes, the spec should change first
- Implementation should stay aligned with the spec

### 3. Minimal Context

- Keep maintenance-critical information in a small number of files
- Avoid repeating the same explanation across many docs
- Read only the code needed for the task

### 4. Verifiable

- Every module should have `tests/smoke.py`
- Validation should actually run the smoke test, not just check formatting
- Success and failure should be explicit

### 5. Handoff Ready

- Another maintainer should be able to recover the module from `INDEX.md`, `SPEC.md`, and the smoke test
- Change history should be traceable
- Key files should stay discoverable

## Required Module Layout

```text
module_name/
├── INDEX.md
├── SPEC.md
└── tests/
    └── smoke.py
```

## Recommended Files

```text
module_name/
├── CHANGELOG.md
├── src/
├── configs/
└── docs/
```

## Versioning

- Current spec version: `v1.0.1 beta`
- Minimal means thin core, hard contract, and large extension surface

## Extension Direction

The next useful upgrades are:

1. add richer project-local override guidance
2. improve source discovery heuristics
3. add optional machine-readable validation output
