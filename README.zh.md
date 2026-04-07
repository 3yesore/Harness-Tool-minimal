# Harness Tool 1.0.1

[English](README.md) | [中文](README.zh.md)

`Harness Tool 1.0.1` 是一个面向模块开发、维护、交接和 AI 协作的 **contract-first 工程基底**。

它的目标不是把仓库做成厚平台，而是把模块职责、接口、验证、关键边界和交接信息收拢到少量固定入口中，让人和 AI 都能在同一套约束下工作。

这一版的重点很明确：

- 把 `core` 做硬
- 把 `contract` 讲清
- 把扩展边界限制在外层
- 把 OpenHarness 支持做成真实可验证的 bridge

## 当前定位

`Harness Tool` 在这条线上承担的是 **上游基底** 角色。

- `harness_core` 负责协议、验证、阶段和 scaffold 语义
- `profiles / templates / markers / overrides` 负责项目侧的可控变化
- OpenHarness 作为外部 runtime 接入，不进入 `core`

所以这个仓库的主线是：

> 先把项目结构和合同做稳定，再通过 bridge 把外部 agent runtime 接进来。

而不是：

> 把 `Harness Tool` 做成 runtime 宿主平台。

## 为什么存在

很多仓库的问题不是“功能不够多”，而是：

- 核心太软，扩展一多就散
- 核心太厚，后续接入越来越重
- 文档、验证、结构、交接是分裂的
- AI 接入时缺少稳定上下文，只能反复猜

`Harness Tool 1.0.1` 对这些问题的处理方式是：

- **thin core**
- **hard contract**
- **explicit extension boundaries**
- **project-owned customization**
- **bridge-side external integration**

## 你会得到什么

### Contract-first 基线

仓库会用固定入口表达模块是什么、怎么验证、哪些边界不能破：

- `INDEX.md`
- `SPEC.md`
- `CHANGELOG.md`
- `validate`
- `marker`

### 薄而硬的核心

`harness_core` 只保留机制，不托管外部 runtime，不吞项目私有语义。

当前固定的协议骨架：

- `CORE_PROTOCOL.md`
- `ADAPTER_PROTOCOL.md`
- `EXTENSION_PROTOCOL.md`

### 受控的扩展空间

扩展可以长，但必须长在边界之外：

- `profiles/`
- `templates/`
- `adapters/`
- `.openclaw_skill/`
- `examples/local_extension/`

### 可验证的 OpenHarness 兼容路径

这一版已经有一条真实存在的 OpenHarness-compatible bridge，而不是口头兼容。

## 推荐和 OpenHarness 一起使用

如果你的目标是：

- 让仓库具备稳定的工程合同
- 再接入 agent runtime 做执行、工具调用和工作流编排

那么 **推荐把 `Harness Tool 1.0.1` 和 OpenHarness 搭配使用**。

两者分工是清楚的：

### Harness Tool

负责：

- 工程合同
- 模块结构
- 验证入口
- 边界纪律
- 交接与维护基线

### OpenHarness

负责：

- agent runtime
- tools / providers
- middleware 组合
- 执行流和外部运行时能力

### 为什么这种组合更合理

`Harness Tool` 更适合做上游，因为它擅长稳定项目语义。  
OpenHarness 更适合做下游，因为它擅长运行 agent。

因此推荐模型是：

> `Harness Tool` 定义项目结构与合同，OpenHarness 消费这些结构去执行。

## OpenHarness 支持现状

当前版本已经具备：

- OpenHarness bridge 文档
- SDK binding 文档
- `harness_validate` process transport
- repo-internal OpenHarness example
- repo-external OpenHarness verification
- runtime-side registration example
- provider / middleware bridge-side metadata contract

相关入口：

- [OPENHARNESS_BRIDGE.md](OPENHARNESS_BRIDGE.md)
- [OPENHARNESS_SDK_BINDING.md](OPENHARNESS_SDK_BINDING.md)
- [OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md](OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md)
- [docs/OPENHARNESS_EXTERNAL_VERIFY.md](docs/OPENHARNESS_EXTERNAL_VERIFY.md)
- [docs/OPENHARNESS_BRIDGE_INDEX.md](docs/OPENHARNESS_BRIDGE_INDEX.md)

### 这版支持什么

- narrow bridge / binding
- context injection
- transport-based validation calls
- repo-external compatibility verification

### 这版不宣称什么

- 不宣称完整 OpenHarness runtime integration
- 不宣称 live provider wiring
- 不宣称 live middleware wiring
- 不宣称 session / conversation integration
- 不宣称 `harness_core` 宿主 runtime

这不是能力缺失被隐藏，而是刻意保留边界。

## 仓库结构

### Core

- `harness_core/`
- `tools/`
- `CORE_PROTOCOL.md`
- `ADAPTER_PROTOCOL.md`
- `EXTENSION_PROTOCOL.md`

### Docs

- `README.md`
- `README.zh.md`
- `INDEX.md`
- `HARNESS_SPEC.md`
- `VERSION_ROADMAP.md`
- `DESIGN_REVIEW.md`
- `AI_CHECKLIST.md`
- `AI_OPERATIONS.md`

### Extensions

- `profiles/`
- `templates/`
- `.openclaw_skill/`
- `examples/local_extension/`

### OpenHarness Bridge

- `adapters/`
- `scripts/openharness_*`
- `examples/openharness_app/`
- `docs/OPENHARNESS_*.md`

### Release

- `GITHUB_RELEASE.md`
- `RELEASE_NOTES_v1.0.1_beta.md`
- `release/v1.0.1-beta/`

## 快速开始

### 初始化新模块

```bash
python tools/init_module.py my_module
```

### 为现有模块补齐 harness

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

### 运行内置示例

```bash
python examples/hello_world/tests/smoke.py
python examples/local_extension/harness/run_harness.py
```

### OpenHarness 兼容示例

```bash
python tools/validate_module.py examples/openharness_app --strict --profile default
```

外部验证：

```bash
cd C:/Users/Y2516/Desktop/openharness_app_external_verify
npm run build
npm run smoke
```

## 已验证结果

当前仓库已通过：

- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python tools/validate_module.py examples/local_extension --strict --profile default`
- `python tools/validate_module.py examples/openharness_app --strict --profile default`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`

外部 OpenHarness app 已通过：

- `npm run build`
- `npm run smoke`

## 版本说明

`Harness Tool 1.0.1` 是一个冻结和收口版本，不是平台化扩张版本。

它现在适合被描述为：

- 一个独立的上游工程基底
- 一个 contract-first 模块框架
- 一个带有 OpenHarness-compatible bridge 的真实仓库

但它仍然应该被准确描述为：

> **core 稳定，bridge 可用，runtime 不宿主。**

## 发布入口

- [GITHUB_RELEASE.md](GITHUB_RELEASE.md)
- [RELEASE_NOTES_v1.0.1_beta.md](RELEASE_NOTES_v1.0.1_beta.md)
- [release/v1.0.1-beta/README.md](release/v1.0.1-beta/README.md)
- [release/v1.0.1-beta/VERSION_DESCRIPTION.zh.md](release/v1.0.1-beta/VERSION_DESCRIPTION.zh.md)
- [release/v1.0.1-beta/PUBLISH_CHECKLIST.zh.md](release/v1.0.1-beta/PUBLISH_CHECKLIST.zh.md)

## 整理与冻结入口

- [docs/CURRENT_CHANGESET_INDEX.md](docs/CURRENT_CHANGESET_INDEX.md)
- [docs/FREEZE_GROUPS.md](docs/FREEZE_GROUPS.md)
- [docs/STAGED_COMMIT_PLAN.md](docs/STAGED_COMMIT_PLAN.md)
- [docs/WORK_INDEX.md](docs/WORK_INDEX.md)
