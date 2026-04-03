# Harness Tool 主索引

## 仓库概览

Harness Tool Minimal 是一套面向模块维护的 Harness Engineering 工具仓库。它的目标不是做成复杂框架，而是把模块职责、接口、验证和交接信息收拢到少量固定文件里，方便人和 AI 接手。

当前仓库已经是可运行的最小闭环，核心能力包括：

- 新建模块骨架
- 为现有模块补 Harness 结构
- 校验模块文档、配置和冒烟测试
- 使用 `profiles/` 做轻量规则预设
- 通过 `.openclaw_skill/` 提供 OpenClaw / Codex Skill 版本
- 通过 GitHub Actions 做基础自动校验

## 仓库结构

```text
harness_tool/
├── README.md
├── README.en.md
├── HARNESS_SPEC.md
├── HARNESS_SPEC.en.md
├── INDEX.md
├── INDEX.en.md
├── VERSION_ROADMAP.md
├── VERSION_ROADMAP.en.md
├── GITHUB_RELEASE.md
├── GITHUB_RELEASE.en.md
├── LICENSE
├── docs/
│   ├── README.md
│   ├── README.en.md
│   ├── AI_CHECKLIST.md
│   ├── AI_REPAIR_GUIDE.md
│   ├── CONTRIBUTING.md
│   ├── DESIGN_REVIEW.md
│   ├── FAQ.md
│   ├── GITHUB_PUBLISH_GUIDE.md
│   ├── RELEASE_NOTES_v1.0.md
│   ├── AI_OPERATIONS.md
│   ├── AI_OPERATIONS.en.md
│   ├── EXTENSION_POINTS.md
│   ├── EXTENSION_POINTS.en.md
│   └── ...
├── .github/
│   └── workflows/validate.yml
├── templates/
├── tools/
├── examples/
├── profiles/
└── .openclaw_skill/
```

## 核心文件说明

### 规范与路线

- [HARNESS_SPEC.md](HARNESS_SPEC.md)：仓库级 Harness 规范，说明什么是 Harness、哪些文件必须有、验证规则是什么
- [VERSION_ROADMAP.md](VERSION_ROADMAP.md)：版本规划，说明当前版本和后续方向
- [GITHUB_RELEASE.md](GITHUB_RELEASE.md)：发布到 GitHub 前的检查步骤

### 工具脚本

- [tools/init_module.py](tools/init_module.py)：初始化新模块骨架
- [tools/apply_harness.py](tools/apply_harness.py)：为现有模块补 Harness
- [tools/validate_module.py](tools/validate_module.py)：校验模块结构、配置文件和冒烟测试

### 模板文件

- `templates/INDEX.md.template`
- `templates/SPEC.md.template`
- `templates/CHANGELOG.md.template`

### 示例模块

- `examples/hello_world/`：最小参考示例，验证链路最清晰
- `examples/user_service/`：稍复杂的参考示例，包含多文件和配置

### 配置预设

- `profiles/default.rules.json`
- `profiles/python-service.rules.json`
- `profiles/README.md`

### 自动化与 Skill

- `.github/workflows/validate.yml`：GitHub Actions 自动校验
- `.openclaw_skill/SKILL.md`：OpenClaw Skill 入口

### 辅助文档

- [docs/README.md](docs/README.md)：文档中心索引

## 快速上手

### 初始化新模块

```bash
python tools/init_module.py <module_name> [--path <output_dir>]
```

默认会生成：

- `INDEX.md`
- `SPEC.md`
- `CHANGELOG.md`
- `src/main.py`
- `tests/smoke.py`
- `configs/default.json`

### 为现有模块补 Harness

```bash
python tools/apply_harness.py <module_path>
python tools/apply_harness.py <module_path> --profile python-service
```

### 校验模块

```bash
python tools/validate_module.py <module_path>
python tools/validate_module.py <module_path> --strict
python tools/validate_module.py <module_path> --strict --profile python-service
```

### 运行示例

```bash
python examples/hello_world/tests/smoke.py
python examples/user_service/tests/smoke.py
```

## 接入现有模块

1. 先读模块自己的 `INDEX.md`
2. 再读模块自己的 `SPEC.md`
3. 只按任务读取相关代码文件
4. 修改实现时同步更新 `SPEC.md` 和 `INDEX.md`
5. 补好 `tests/smoke.py`
6. 运行 `tools/validate_module.py <module_path>`
7. 变更行为时更新 `CHANGELOG.md`

## 版本信息

- 当前版本：`v1.0.0 Minimal`
- 规范版本：`v1.0`
- 当前状态：可运行、可验证、适合发布前整理
- 最后更新：2026-04-03
