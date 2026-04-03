---
name: harness
description: Apply harness engineering principles to make modules AI-maintainable. Use when: (1) creating new modules that need to be maintained across sessions/agents, (2) refactoring existing code for better AI handoff, (3) establishing project-wide maintenance standards, (4) debugging modules with poor documentation or unclear interfaces. Harness focuses on: standardized I/O, clear indexing, minimal context dependency, verifiable contracts, and cross-session continuity.
---

# Harness Engineering

Make modules AI-maintainable through standardized interfaces, clear indexing, and verifiable contracts.

## Core Principles

1. **Index-first**: Every module has INDEX.md (responsibilities, key files, dependencies)
2. **Standardized I/O**: Inputs/outputs follow consistent schemas
3. **Minimal context**: Key info in index + spec, code read on-demand
4. **Verifiable**: Every module has smoke tests with clear pass/fail
5. **Handoff-ready**: New AI can take over via index + spec alone

## When to Use

- Creating new modules for long-term maintenance
- Refactoring code for better AI handoff
- Establishing project-wide standards
- Debugging poorly-documented modules

## Module Structure

```
module_name/
├── INDEX.md           # Module index (required)
├── SPEC.md            # Interface spec (required)
├── CHANGELOG.md       # Change history (recommended)
├── src/               # Source code
├── tests/             # Tests
├── configs/           # Configuration
└── docs/              # Detailed docs (optional)
```

## Quick Reference (5 Most Common Operations)

```bash
# 1. Initialize new module
python scripts/init_harness_module.py my_module

# 2. Apply harness to existing code
python scripts/apply_harness.py existing_module

# 3. Validate module compliance
python scripts/validate_harness.py my_module

# 4. Run module tests
python my_module/tests/smoke.py

# 5. Check what AI should read
cat my_module/INDEX.md my_module/SPEC.md
```

**AI Workflow**: Read INDEX.md + SPEC.md → Code selectively → Change → Test → Update CHANGELOG

See `references/` for full templates and detailed guidance.

## Quick Start

### Initialize New Module

```bash
python scripts/init_harness_module.py <module_name> [--path <output_dir>]
```

This creates the full structure with templates.

### Validate Existing Module

```bash
python scripts/validate_harness.py <module_path>
```

Checks for required files, interface consistency, and test coverage.

### Apply to Existing Code

1. Read the module's current structure
2. Create INDEX.md documenting responsibilities and key files
3. Create SPEC.md defining inputs/outputs/errors
4. Add smoke tests to tests/
5. Run validator to verify compliance

## INDEX.md Template

See `references/index_template.md` for the full template with examples.

Key sections:
- **Responsibilities**: One-line module purpose
- **Key Files**: Entry points, configs, tests
- **Dependencies**: External and internal deps
- **Quick Validation**: How to verify it works
- **Maintenance Notes**: Constraints, known issues

## SPEC.md Template

See `references/spec_template.md` for the full template with examples.

Key sections:
- **Input**: Parameters, types, constraints
- **Output**: Success/error formats, status codes
- **Configuration**: Config files, env vars, defaults
- **Error Handling**: Error types and recovery strategies
- **Examples**: Complete usage examples

## Validation

The validator checks:
- Required files exist (INDEX.md, SPEC.md)
- INDEX.md has all required sections
- SPEC.md defines I/O contracts
- Tests directory exists with runnable tests
- Config files are valid JSON/YAML
- Cross-references are valid

Run after any changes:
```bash
python scripts/validate_harness.py <module_path> --strict
```

## AI Workflow

When maintaining a harness-compliant module:

1. **Locate**: Read main index to find target module
2. **Understand**: Read INDEX.md + SPEC.md (not full code)
3. **Read selectively**: Only read code files relevant to task
4. **Execute**: Make changes following spec constraints
5. **Verify**: Run smoke tests
6. **Document**: Update CHANGELOG.md with changes

## Integration with Existing Projects

For projects like `5090_qwen_business`:

1. Identify core modules (e.g., runtime/controller, runtime/dispatch)
2. Add INDEX.md to each module documenting current state
3. Add SPEC.md defining actual interfaces
4. Add smoke tests for critical paths
5. Run validator to ensure compliance
6. Update main project INDEX.md to reference modules

## Resources

### scripts/
- `init_harness_module.py`: Initialize new harness-compliant module
- `validate_harness.py`: Validate module compliance
- `apply_harness.py`: Apply harness to existing code (interactive)

### references/
- `index_template.md`: Full INDEX.md template with examples
- `spec_template.md`: Full SPEC.md template with examples
- `harness_spec.md`: Complete harness specification
- `validation_rules.md`: Detailed validation criteria
