# Harness Tool Minimal v1.0.1 beta

[![Validate](https://github.com/3yesore/Harness-Tool-minimal/actions/workflows/validate.yml/badge.svg)](https://github.com/3yesore/Harness-Tool-minimal/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](../../LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.1-beta-blue.svg)](../VERSION_ROADMAP.en.md)

This is a beta release package focused on tightening and hardening the minimal baseline.  
It keeps the smallest complete Harness workflow while clarifying the standard entry points, validation flow, and extension boundaries. It is best suited for small projects, small modules, and early-stage development.

## Focus of this release

- Keep the minimal `init / apply / validate` loop
- Keep the handoff-friendly structure around `INDEX.md`, `SPEC.md`, `CHANGELOG.md`, and `tests/smoke.py`
- Keep `profiles/`, `templates/`, and `.openclaw_skill/` as lightweight extension surfaces
- Continue using GitHub Actions for baseline validation
- Keep the Chinese primary docs plus English mirrors release format

## What you get

- A minimal loop: initialize, retrofit, validate, record
- Real validation: `validate_module.py` actually runs `tests/smoke.py`
- Lightweight extension surfaces: `profiles/`, `templates/`, and `.openclaw_skill/`
- A release-ready package: Chinese homepage, English mirror, release notes, and checklist

## Who this is for

- People who want a module to be handoff-friendly and verifiable
- People who need `INDEX.md`, `SPEC.md`, and `CHANGELOG.md` in an existing project
- People who want the same workflow available in OpenClaw and Codex
- People who want to put a module under the Harness workflow early in development

## Included files

- `README.md` / `README.en.md`
- `VERSION_DESCRIPTION.zh.md` / `VERSION_DESCRIPTION.en.md`
- `GITHUB_RELEASE.zh.md` / `GITHUB_RELEASE.en.md`
- `MANIFEST.md`
- `PUBLISH_CHECKLIST.zh.md` / `PUBLISH_CHECKLIST.en.md`

## Version description

See the full version description here:

- [VERSION_DESCRIPTION.zh.md](VERSION_DESCRIPTION.zh.md)
- [VERSION_DESCRIPTION.en.md](VERSION_DESCRIPTION.en.md)

