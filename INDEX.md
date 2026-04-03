# Harness Tool 主索引

## 仓库概览

Harness Tool Minimal 是一套面向模块维护的 Harness Engineering 工具仓库。它的目标不是做成复杂框架，而是把模块的职责、接口、验证和交接信息收拢到少量固定文件里，方便人和 AI 接手维护。

当前仓库已经是可运行的最小闭环，核心能力包括：

- 新建模块骨架
- 为现有模块补 Harness 结构
- 校验模块文档、配置和冒烟测试
- 使用 `profiles/` 做轻量规则预设
- 通过 `.openclaw_skill/` 提供 OpenClaw Skill 版本
- 通过 GitHub Actions 做基础自动校验

## 仓库结构

```text
harness_tool/
├── README.md
├── HARNESS_SPEC.md
├── INDEX.md
├── VERSION_ROADMAP.md
├── GITHUB_RELEASE.md
├── RELEASE_NOTES_v1.0.md
├── LICENSE
├── .gitignore
├── .github/
│   └── workflows/validate.yml
├── templates/
│   ├── INDEX.md.template
│   ├── SPEC.md.template
│   └── CHANGELOG.md.template
├── tools/
│   ├── init_module.py
│   ├── apply_harness.py
│   └── validate_module.py
├── examples/
│   ├── hello_world/
│   └── user_service/
├── profiles/
│   ├── default.rules.json
│   ├── python-service.rules.json
│   └── README.md
└── .openclaw_skill/
    ├── SKILL.md
    ├── scripts/
    ├── references/
    ├── templates/
    └── profiles/
```

## 核心文件说明

### 规范与说明

- [HARNESS_SPEC.md](HARNESS_SPEC.md)：仓库级 Harness 规范，说明什么是 Harness、哪些文件必须有、验证规则是什么
- [VERSION_ROADMAP.md](VERSION_ROADMAP.md)：版本规划，说明当前版本和后续方向
- [GITHUB_RELEASE.md](GITHUB_RELEASE.md)：发布到 GitHub 前的检查步骤
- [RELEASE_NOTES_v1.0.md](RELEASE_NOTES_v1.0.md)：当前版本的发布说明

### 工具脚本

- [tools/init_module.py](tools/init_module.py)：初始化新模块骨架
- [tools/apply_harness.py](tools/apply_harness.py)：为现有模块补 Harness 文件和冒烟测试
- [tools/validate_module.py](tools/validate_module.py)：校验模块结构、配置文件和冒烟测试

### 模板文件

- `templates/INDEX.md.template`
- `templates/SPEC.md.template`
- `templates/CHANGELOG.md.template`

### 示例模块

- `examples/hello_world/`：最小参考示例，验证链路最清晰
- `examples/user_service/`：稍复杂的参考示例，包含多文件和配置

### 配置预设

- `profiles/default.rules.json`：默认规则
- `profiles/python-service.rules.json`：Python 服务型模块规则
- `profiles/README.md`：当前 profile 支持状态说明

### 自动化与 Skill

- `.github/workflows/validate.yml`：GitHub Actions 自动校验
- `.openclaw_skill/SKILL.md`：OpenClaw Skill 入口

## 快速开始

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
4. 修改实现时同步更新 `SPEC.md` 或 `INDEX.md`
5. 跑 `tests/smoke.py`
6. 跑 `tools/validate_module.py <module_path>`
7. 变更行为时更新 `CHANGELOG.md`

## 模块清单

### 示例模块

- `examples/hello_world/`：最小验证示例
- `examples/user_service/`：多文件模块示例

### 预设规则

- `profiles/default.rules.json`
- `profiles/python-service.rules.json`

### 维护中的仓库能力

- 模块初始化
- 模块接入
- 模块验证
- OpenClaw Skill 包装
- GitHub 自动校验

## 维护指南

### 新建模块

1. 用 `init_module.py` 生成骨架
2. 补齐模块逻辑
3. 填写模块 `INDEX.md` 和 `SPEC.md`
4. 补充或修改 `tests/smoke.py`
5. 运行 `validate_module.py`
6. 更新 `CHANGELOG.md`

### 维护已有模块

1. 先看模块 `INDEX.md` 和 `SPEC.md`
2. 按需修改相关代码
3. 如果接口变了，先改 `SPEC.md`
4. 如果关键文件变了，先改 `INDEX.md`
5. 跑冒烟测试
6. 跑验证工具

### 维护仓库本身

- 文档口径要和脚本行为一致
- 例子要和脚本验证逻辑一致
- `.openclaw_skill/` 要和仓库脚本同步
- 发布前先跑例子和验证

## OpenClaw Skill

仓库同时提供了 `.openclaw_skill/` 版本，方便单独安装到 OpenClaw 环境中使用。  
如果只拿 skill，也能获得当前这套最小闭环：初始化、接入、验证、模板和规则预设。

## 版本信息

- 当前版本：`v1.0.0 Minimal`
- 规范版本：`v1.0`
- 当前状态：可运行、可验证、适合发布前整理
- 最后更新：2026-04-03
