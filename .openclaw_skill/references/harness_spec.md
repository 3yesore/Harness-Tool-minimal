# Harness Specification v1.0

## What Harness Means Here

Harness Engineering in this repository is a module-maintenance contract:

- keep the important context in `INDEX.md` and `SPEC.md`
- keep validation runnable
- keep handoff cheap for the next human or AI

It is not trying to be a full framework, package manager, or build system.

## Core Principles

### 1. Index-first

- Every maintained module should have an `INDEX.md`
- The index should explain responsibility, key files, dependencies, and the quick validation path
- Consumers should read the index before scanning code

### 2. Contract-driven

- `SPEC.md` should describe the module's public inputs, outputs, configuration, and error handling
- The module implementation should follow the contract unless the contract is intentionally changed

### 3. Minimal context

- Put the maintenance-critical information in a small number of files
- Avoid duplicating the same explanation in many places

### 4. Verifiable

- Every module should have a runnable smoke test
- Validation should include both document checks and test execution

### 5. Handoff-ready

- Another maintainer should be able to recover the module quickly from `INDEX.md`, `SPEC.md`, and the smoke test

## Current Repository Scope

The current implementation is Python-first.

- `scripts/init_harness_module.py` creates a Python-oriented module skeleton
- `scripts/apply_harness.py` generates Harness docs and a smoke test when needed
- `scripts/validate_harness.py` checks the docs, parses configs, and executes `tests/smoke.py`
- `profiles/` is wired into the CLI through `--profile`, but the current rule files are still minimal

## Required Module Layout

```text
module_name/
├── INDEX.md
├── SPEC.md
├── CHANGELOG.md
├── tests/
│   └── smoke.py
├── src/
├── configs/
└── docs/
```

The `CHANGELOG.md`, `src/`, `configs/`, and `docs/` directories are recommended, but the current validator only requires the docs, tests, and valid config files when present.

## INDEX.md Contract

`INDEX.md` should contain these sections:

- `## 职责`
- `## 关键文件`
- `## 依赖`
- `## 快速验证`

Recommended extra sections:

- `## 维护注意事项`
- `## 最后更新`

The quick verification section should point to a real executable command, ideally `python tests/smoke.py`.

## SPEC.md Contract

`SPEC.md` should contain these sections:

- `## 输入`
- `## 输出`
- `## 配置`
- `## 错误处理`
- `## 示例`

The contract should be specific enough that a maintainer can tell what is allowed, what is rejected, and what a successful call looks like.

## Smoke Test Contract

The smoke test should:

- be runnable with `python tests/smoke.py`
- exit with code `0` when it passes
- print a clear success or failure message
- cover the module's most important path, not just importability

## Validation Rules

The current validator does the following:

- checks that `INDEX.md` and `SPEC.md` exist
- warns if `CHANGELOG.md` is missing
- verifies key sections in `INDEX.md` and `SPEC.md`
- checks that config files in `configs/` are valid JSON
- checks that `tests/` exists and contains at least one `.py` file
- executes `tests/smoke.py` when it exists
- supports `--profile` to load rule presets from `profiles/*.rules.json`

Known limitations:

- validation is structural plus smoke execution, not full semantic verification
- it is Python-execution based, so non-Python modules need more work
- cross-file contract inference is still heuristic

## Current Gaps

- `apply_harness.py` still relies on heuristics rather than actual source parsing
- the repository does not yet have cross-language templates
- profile rules are currently minimal and mostly mirror the default behavior

## Versioning

- Current spec version: `v1.0`
- Minimal means "usable and verifiable", not "fully generalized"

## Extension Direction

The next useful upgrades are:

1. add language presets beyond Python
2. improve `apply_harness.py` to infer entry points and test files more accurately
3. add a non-Python validation path when those presets exist
