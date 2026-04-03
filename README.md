# Harness Tool Minimal

Harness Tool Minimal 是一个面向模块维护的 Harness Engineering 工具仓库。它的目标不是做成复杂框架，而是把模块的职责、接口、验证和交接信息收拢到少量固定文件里，方便人和 AI 接手维护。

当前仓库是一个可运行的最小闭环，核心能力包括：

- 新建模块骨架
- 为现有模块补 Harness 结构
- 校验模块文档、配置和冒烟测试
- 使用 `profiles/` 做轻量规则预设
- 通过 `.openclaw_skill/` 提供 OpenClaw Skill 版本
- 通过 GitHub Actions 做基础自动校验

## 双语文档

仓库现在维护两套并行文档：

- 中文版：`README.md`、`INDEX.md`、`HARNESS_SPEC.md`、`GITHUB_RELEASE.md`、`VERSION_ROADMAP.md`、`AI_OPERATIONS.md`、`EXTENSION_POINTS.md`
- 英文版：`README.en.md`、`INDEX.en.md`、`HARNESS_SPEC.en.md`、`GITHUB_RELEASE.en.md`、`VERSION_ROADMAP.en.md`、`AI_OPERATIONS.en.md`、`EXTENSION_POINTS.en.md`

如果你习惯英文文档，可以直接打开对应的 `.en.md` 文件。

## 核心流程

1. 先读模块的 `INDEX.md`
2. 再读模块的 `SPEC.md`
3. 只修改和任务直接相关的代码
4. 跑冒烟测试
5. 跑验证工具
6. 行为变化时更新 `CHANGELOG.md`

## 快速开始

### 初始化新模块

```bash
python tools/init_module.py my_module
```

### 为现有模块补 Harness

```bash
python tools/apply_harness.py path/to/module
python tools/apply_harness.py path/to/module --profile python-service
```

### 校验模块

```bash
python tools/validate_module.py path/to/module
python tools/validate_module.py path/to/module --strict
python tools/validate_module.py path/to/module --strict --profile python-service
```

### 运行示例

```bash
python examples/hello_world/tests/smoke.py
python examples/user_service/tests/smoke.py
```

## 文档入口

- [HARNESS_SPEC.md](HARNESS_SPEC.md) 仓库级规范
- [INDEX.md](INDEX.md) 仓库结构说明
- [README.en.md](README.en.md) 英文入口
- [GITHUB_RELEASE.md](GITHUB_RELEASE.md) 发布准备
- [VERSION_ROADMAP.md](VERSION_ROADMAP.md) 版本规划
- [profiles/README.md](profiles/README.md) profile 状态说明
- [.openclaw_skill/SKILL.md](.openclaw_skill/SKILL.md) OpenClaw Skill 入口

## 当前状态

- 验证链路已经跑通
- 示例模块 `examples/hello_world` 可正常通过冒烟测试
- skill 包和仓库实现保持同步
- 当前仓库仍然是发布前的整理版，不是最终发布仓库

## 备注

- 本仓库保持 Python-first，但文档结构是模块化的
- `apply_harness.py` 目前仍是启发式接入，不是深度源码分析器
- profile 规则目前比较轻量，主要是把默认规则显式化
