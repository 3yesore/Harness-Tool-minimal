# Harness Validation Rules

## Required Files

### INDEX.md
- Must exist
- Must contain:
  - `## 职责`
  - `## 关键文件`
  - `## 调用入口`
  - `## 关键标记`
  - `## 依赖`
  - `## 快速验证`
- Recommended:
  - `## 维护注意事项`
  - `## 变更记录`

### SPEC.md
- Must exist
- Must contain:
  - `## 输入`
  - `## 调用入口`
  - `## 输出`
  - `## 配置`
  - `## 错误处理`
  - `## 示例`
  - `## 关键标记`

## Recommended Files

### CHANGELOG.md
- Recommended
- Should record the important history of the module
- Suggested format: date + change type + description

### tests/
- Must exist
- Should contain at least one runnable `.py` test
- The test should print clear pass/fail output
- `tests/smoke.py` is the preferred entry point

### configs/
- Optional
- If present, JSON files must be valid

## Marker Rules

The frozen protocol treats these marker keys as the core contract:

- `entry_file`
- `call_path`
- `call_entry`

Recommended marker keys:

- `smoke_test`
- `config`
- `marker_source`

## Profile Rules

Profiles are loaded from `profiles/*.rules.json` and can adjust:

- required files
- recommended files
- required `INDEX.md` sections
- required `SPEC.md` sections
- recommended directories for scaffolding
- entry consistency mode
- marker consistency mode

The bundled profiles are intentionally minimal:

- `default`
- `python-service`

## Validation Levels

### Errors
- missing required files
- missing required sections
- invalid config files
- missing tests directory
- missing required marker paths

### Warnings
- missing recommended files
- missing recommended sections
- empty tests directory
- missing configs directory when a module should have one
- entry mismatch when the profile keeps consistency in soft mode

## Strict Mode

When `--strict` is enabled:

- warnings are treated as errors
- validation fails with a non-zero exit code

## Smoke Test Execution

The validator executes `tests/smoke.py` when it exists.

- it must exit `0` on success
- it must provide clear output
- it should cover the module's main path, not just importability
