# Harness Specification v1.0

## What Harness Means Here

In this repository, Harness is a module-maintenance contract. It is not a full framework or package manager. The goal is to keep the important maintenance context in a few files so that a human or AI can take over quickly.

This repository focuses on:

- a clear `INDEX.md`
- a clear `SPEC.md`
- a runnable smoke test
- lightweight automation
- low handoff cost

## Current Repository Scope

The implementation is currently Python-first, but the repository itself is module-oriented rather than tied to a specific business domain.

Implemented today:

- `tools/init_module.py` creates a module skeleton
- `tools/apply_harness.py` adds Harness files and a smoke test to an existing module
- `tools/validate_module.py` validates docs, configs, and `tests/smoke.py`
- `profiles/` is wired into the CLI through `--profile`
- `.openclaw_skill/` packages the same workflow as a skill

Deep language-agnostic support is not implemented yet, so non-Python modules still need extra work.

## Core Principles

### 1. Index First

- Every maintained module should have an `INDEX.md`
- `INDEX.md` should explain responsibilities, key files, dependencies, and the validation entry point
- AI should read the index before scanning code

### 2. Contract Driven

- `SPEC.md` should define inputs, outputs, configuration, and error handling
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

## INDEX.md Contract

The `INDEX.md` file should contain at least:

- `## Responsibilities`
- `## Key Files`
- `## Dependencies`
- `## Quick Validation`

Recommended extras:

- `## Maintenance Notes`
- `## Last Updated`

The quick validation section should point to a real command, ideally:

```bash
python tests/smoke.py
```

## SPEC.md Contract

The `SPEC.md` file should contain at least:

- `## Input`
- `## Output`
- `## Configuration`
- `## Error Handling`
- `## Example`

The spec should be specific enough that a maintainer can tell what is allowed, what is rejected, and what success looks like.

## Smoke Test Contract

The smoke test should:

- run with `python tests/smoke.py`
- exit with code `0` on success
- print a clear success or failure message
- cover the module's main path

The current validator executes `tests/smoke.py` when it exists.

## Validation Rules

Current `tools/validate_module.py` behavior:

- checks for `INDEX.md` and `SPEC.md`
- warns if `CHANGELOG.md` is missing
- checks required sections in `INDEX.md`
- checks required sections in `SPEC.md`
- validates JSON files in `configs/`
- checks that `tests/` exists and contains at least one `.py` file
- runs `tests/smoke.py`
- applies additional checks from `--profile`

Current `tools/apply_harness.py` behavior:

- reads the module directory structure
- generates `INDEX.md`, `SPEC.md`, and `CHANGELOG.md` when missing
- creates recommended directories from the active profile
- creates `tests/smoke.py` when the tests directory is missing or empty

## Profile Support

Profile support is wired through `--profile`.

Current rule files:

- `profiles/default.rules.json`
- `profiles/python-service.rules.json`

Profiles are currently used for:

- required files
- recommended files
- recommended directories
- required `INDEX.md` / `SPEC.md` sections

The profiles are intentionally lightweight and mostly mirror the default behavior.

## Current Limitations

- The repository is Python-first
- `apply_harness.py` still uses heuristics instead of deep source analysis
- Validation is structural plus smoke execution, not full semantic verification
- Non-Python modules still need additional design

## AI Workflow

When maintaining a Harness module:

1. Read the module's `INDEX.md`
2. Read the module's `SPEC.md`
3. Read only the code files needed for the task
4. Update the spec when the interface changes
5. Run `tests/smoke.py`
6. Run `tools/validate_module.py`
7. Update `CHANGELOG.md` when behavior changes

## Versioning and Direction

- Current spec version: `v1.0`
- Current goal: usable, verifiable, handoff-ready
- Next direction: better source discovery, richer profile differences, more language support

## References

- [INDEX.en.md](INDEX.en.md)
- [README.en.md](README.en.md)
- [tools/validate_module.py](tools/validate_module.py)
- [tools/apply_harness.py](tools/apply_harness.py)
- [profiles/README.md](profiles/README.md)
- [.openclaw_skill/SKILL.md](.openclaw_skill/SKILL.md)
