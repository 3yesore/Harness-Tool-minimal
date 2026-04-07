# Harness Tool 1.0.1 Release Package

[English](README.en.md) | [中文](README.md)

This is the release preparation package for `Harness Tool 1.0.1`.

## Purpose

- collect the version-facing materials for the current freeze baseline
- provide one entry point for pre-release checks
- provide a version reference package for post-release review

## Current Release Judgment

- this version is suitable as the baseline release of your own project
- the core direction remains:
  - `harness_tool` is the upstream, contract-first base
  - `harness_core` remains thin and does not host runtime behavior
  - OpenHarness compatibility stays in the bridge / binding layer
- the current repository already has:
  - a frozen core / contract baseline
  - a synced skill mirror
  - an OpenHarness-compatible bridge
  - repo-external verification evidence

## Main Files In This Package

- [VERSION_DESCRIPTION.zh.md](VERSION_DESCRIPTION.zh.md)
- [VERSION_DESCRIPTION.en.md](VERSION_DESCRIPTION.en.md)
- [GITHUB_RELEASE.zh.md](GITHUB_RELEASE.zh.md)
- [GITHUB_RELEASE.en.md](GITHUB_RELEASE.en.md)
- [PUBLISH_CHECKLIST.zh.md](PUBLISH_CHECKLIST.zh.md)
- [PUBLISH_CHECKLIST.en.md](PUBLISH_CHECKLIST.en.md)
- [MANIFEST.md](MANIFEST.md)

## Version Boundary

This release package explicitly supports:

- a thin-core, hard-contract repository narrative
- a frozen baseline for templates, rules, examples, and the skill mirror
- an OpenHarness-compatible bridge with repo-external verification

This release package does not claim:

- a full OpenHarness runtime integration
- live provider / middleware wiring
- session / conversation integration

## Suggested Release Strategy

- finish commit grouping first using the repository freeze groups
- then publish `Harness Tool 1.0.1`
- if anything is contributed upstream to OpenHarness afterward, prefer:
  - docs
  - examples
  - compatibility notes

## Suggested Release State

- current state: publishable freeze baseline
- release policy: freeze the baseline and avoid thickening the core
- follow-up policy: accept bug fixes, documentation corrections, compatibility patches, and verified boundary tightening only
