# Harness Tool

[English](README.md) | [中文](README.zh.md)

以契约为先的工程基底，核心保持薄，OpenHarness 通过桥接方式接入。

## 为什么会有这个项目

很多仓库最后会坏在两个方向上：

- 核心太软，结构和校验规则会慢慢漂移
- 核心太厚，每接一个新系统都把更多运行时逻辑拖进仓库基底

Harness Tool 要解决的是这个中间地带：

- 保持核心小
- 把合同讲清楚
- 让扩展能变化，但不重写基底
- 让外部 runtime 通过桥接接入，而不是被核心吞进去

## 它是什么

Harness Tool 是：

- 一个上游工程基底
- 一套 contract-first 的仓库结构
- 一套用于校验、初始化和边界控制的工具
- 面向模块开发、维护、交接和 AI 协作的基础设施

在这个仓库里，`harness_core` 负责 protocol、validation、stages 和 scaffold semantics。

## 它不是什么

Harness Tool 不是：

- 完整的 agent runtime
- workflow host
- plugin platform
- OpenHarness 自身的集成层
- 吞并项目私有运行时行为的厚框架

## 架构一览

仓库分成三层：

- `harness_core/`
  负责协议、校验、阶段和 scaffold 语义。
- 扩展层
  `profiles/`、`templates/`、`.openclaw_skill/`，以及 `examples/local_extension/` 这样的本地扩展示例。
- bridge 层
  `adapters/`、`scripts/openharness_*` 和 OpenHarness 示例。

设计目标很直接：合同放在核心，变化留在外层，外部 runtime 通过窄桥接入。

## 和 OpenHarness 的关系

OpenHarness 是外部 runtime。这个仓库不拥有它，也不会把它的运行时职责塞进 `harness_core`。

当前接入方式是 bridge-side 的，包括：

- bridge 和 binding 文档
- 基于 transport 的校验调用
- context injection
- 面向 OpenHarness 的示例
- 外部验证材料

当前这个仓库支持：

- OpenHarness-compatible bridge 和 binding
- 通过 process transport 暴露 `harness_validate`
- 面向 agent / skill 的上下文注入材料
- 位于 core 之外的 runtime-side registration example

当前这个仓库不宣称：

- 完整拥有 OpenHarness runtime
- 在 core 内做 live provider wiring
- 在 core 内做 live middleware wiring
- 完整的 session / conversation integration
- 在仓库内部提供完整 agent 平台

## 快速开始

初始化一个新模块：

```bash
python tools/init_module.py my_module
```

把 Harness Tool 应用到已有模块：

```bash
python tools/apply_harness.py path/to/module
python tools/apply_harness.py path/to/module --profile python-service
```

校验模块：

```bash
python tools/validate_module.py path/to/module
python tools/validate_module.py path/to/module --strict
python tools/validate_module.py path/to/module --strict --profile python-service
```

校验 OpenHarness 示例：

```bash
python tools/validate_module.py examples/openharness_app --strict --profile default
```

外部验证路径见 [OPENHARNESS_EXTERNAL_VERIFY](docs/OPENHARNESS_EXTERNAL_VERIFY.md)。

## 仓库结构

- 根入口
  `README.md`、`README.zh.md`、`README.en.md`。
- `docs/`
  仓库文档、协议、发布说明、工作索引和 OpenHarness bridge 材料。
- `harness_core/`
  共享协议与校验实现。
- `tools/`
  模块初始化、应用、校验和修复入口。
- `examples/`
  基线示例、本地扩展示例和 OpenHarness 示例应用。
- `adapters/`
  bridge-side 协议和 OpenHarness 集成接口。
- `release/`
  打包好的发布材料。

## 当前范围和限制

当前范围是刻意收窄的：

- OpenHarness 支持只停留在 bridge-side
- `harness_core` 不拥有 runtime 职责
- provider 和 middleware 目前只是 bridge metadata，不是 live core wiring
- 完整的 session / conversation integration 不在当前范围内
- `examples/openharness_app` 在本地依赖缺失时可能跳过 npm smoke

这个仓库可以作为工程基底，也可以作为 bridge 来源，但不应该被描述成完整 runtime 产品。

## 继续阅读

- [仓库索引](docs/INDEX.md)
- [Harness 规范](docs/HARNESS_SPEC.md)
- [Core 协议](docs/CORE_PROTOCOL.md)
- [Adapter 协议](docs/ADAPTER_PROTOCOL.md)
- [Extension 协议](docs/EXTENSION_PROTOCOL.md)
- [OpenHarness Bridge](docs/OPENHARNESS_BRIDGE.md)
- [OpenHarness SDK Binding](docs/OPENHARNESS_SDK_BINDING.md)
- [GitHub 发布说明](docs/GITHUB_RELEASE.md)
