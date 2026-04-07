# Harness Tool

[English](README.md) | [中文](README.zh.md)

以契约为先的工程基底，核心保持薄，OpenHarness 通过窄桥接入。

## 这个项目解决什么问题

很多仓库最后会坏在两个方向上：

- 核心太软，结构和校验会慢慢漂移
- 核心太厚，每接一个系统就把更多运行时逻辑拖进基底

Harness Tool 要解决的是中间这条线：

- 合同明确
- 校验可预测
- 扩展边界清楚
- 外部 runtime 能接进来，但不把仓库做成 runtime host

## 它是什么

Harness Tool 是：

- 一个上游工程基底
- 一套 contract-first 的仓库结构
- 一套用于校验和初始化的工具
- 面向模块开发、维护、交接和 AI 协作的基础设施

`harness_core` 负责 protocol、validation、stages 和 scaffold semantics。

## 它不是什么

Harness Tool 不是：

- 完整的 agent runtime
- workflow host
- plugin platform
- OpenHarness 替代品
- 厚框架

## 架构一览

仓库分成三层：

- `harness_core/`
  负责协议、校验、阶段和 scaffold 语义
- 扩展层
  `profiles/`、`templates/`、`.openclaw_skill/` 和本地扩展
- bridge 层
  `adapters/`、`scripts/openharness_*` 和 OpenHarness 示例

合同留在核心，变化留在外层，外部 runtime 通过桥接接入。

## 和 OpenHarness 的关系

OpenHarness 是外部 runtime，不属于这个仓库的 core。

Harness Tool 提供：

- 项目合同
- 校验入口
- 模块上下文
- 边界纪律

OpenHarness 提供：

- agent runtime
- tools 和 providers
- middleware 组合
- 执行流

当前支持是真实的，但范围刻意收窄：

- bridge 和 binding 文档
- `harness_validate` process transport
- context injection
- 仓库内外示例

当前这个仓库不宣称：

- `harness_core` 拥有 runtime 职责
- live provider wiring
- live middleware wiring
- 完整的 session / conversation integration

## 快速开始

初始化一个模块：

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
```

校验 OpenHarness 示例：

```bash
python tools/validate_module.py examples/openharness_app --strict --profile default
```

## 仓库结构

- `README.md`
  主入口
- `docs/`
  协议、规范、集成文档和发布说明
- `harness_core/`
  核心实现
- `tools/`
  init、apply、validate、repair 入口
- `examples/`
  参考模块和 OpenHarness 示例
- `adapters/`
  bridge-side 集成代码
- `release/`
  打包发布材料

## 当前范围和限制

当前范围是刻意收窄的：

- OpenHarness 支持只停留在 bridge-side
- `harness_core` 不宿主 runtime 职责
- provider 和 middleware 仍然留在 core 外
- 完整的 session / conversation integration 不在当前范围内
- `examples/openharness_app` 在本地依赖缺失时可能跳过 npm smoke

这个仓库可以作为工程基底，也可以作为 bridge 来源，但不应该被描述成完整 runtime 产品。

## 文档地图

- [核心文档](docs/core/README.md)
- [扩展文档](docs/extensions/README.md)
- [OpenHarness 集成](docs/integrations/openharness/README.md)
- [运维与维护说明](docs/operations/README.md)
- [发布说明](docs/releases/README.md)
