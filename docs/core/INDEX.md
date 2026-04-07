# Harness Tool 总索引

## 仓库概览

`Harness Tool Minimal` 是一个面向模块开发与维护全生命周期的 `harness kernel` 仓库。它不是厚框架，也不是包管理器，而是把模块职责、接口、验证和交接信息收拢到少量固定文件里，让人和 AI 在开发、接入、演进和维护阶段保持一致。

当前仓库冻结为 `v1.0.1 beta` 基线，核心原则是：

- `core` 只保留机制和合同
- `adapter` 负责外部接入翻译
- `extension` 提供默认预设和模板
- `override` 只允许项目本地覆盖，不能破坏合同

## 协议地图

- [CORE_PROTOCOL.md](CORE_PROTOCOL.md)：冻结 `core` 骨架和工作流阶段
- [ADAPTER_PROTOCOL.md](ADAPTER_PROTOCOL.md)：外部接入翻译层的最小协议
- [EXTENSION_PROTOCOL.md](EXTENSION_PROTOCOL.md)：项目本地扩展的边界
- [../adapters/README.md](../adapters/README.md)：适配器层工作区入口
- [OPEN_ITEMS.md](OPEN_ITEMS.md)：保留未收口事项
- [WORK_INDEX.md](WORK_INDEX.md)：整理顺序索引
- [CURRENT_CHANGESET_INDEX.md](CURRENT_CHANGESET_INDEX.md)：当前变更面的最终收尾索引

## 仓库结构

```text
harness_tool_test/
├── README.md
├── CORE_PROTOCOL.md
├── ADAPTER_PROTOCOL.md
├── EXTENSION_PROTOCOL.md
├── HARNESS_SPEC.md
├── INDEX.md
├── VERSION_ROADMAP.md
├── GITHUB_RELEASE.md
├── RELEASE_NOTES_v1.0.1_beta.md
├── DESIGN_REVIEW.md
├── AI_CHECKLIST.md
├── LICENSE
├── adapters/
├── templates/
├── tools/
├── examples/
├── profiles/
└── .openclaw_skill/
```

## 三层结构

### 1. Core
只负责机制、合同、验证和生成计划。

### 2. Adapter
只负责把 OS / 多 agent / 外部项目翻译成标准输入。

### 3. Extension
只负责项目本地差异，保留 `profiles / templates / marker / override`。

## 核心文件

### 规范与版本
- [HARNESS_SPEC.md](HARNESS_SPEC.md)：仓库级合同与边界说明
- [VERSION_ROADMAP.md](VERSION_ROADMAP.md)：版本路线与冻结基线说明
- [DESIGN_REVIEW.md](DESIGN_REVIEW.md)：minimal 白名单、黑名单和性能底线
- [AI_CHECKLIST.md](AI_CHECKLIST.md)：AI 接手时的执行清单
- [GITHUB_RELEASE.md](GITHUB_RELEASE.md)：发布前检查与打标签说明
- [RELEASE_NOTES_v1.0.1_beta.md](RELEASE_NOTES_v1.0.1_beta.md)：当前 beta 冻结说明

### 协议文件
- [CORE_PROTOCOL.md](CORE_PROTOCOL.md)：core 协议骨架
- [ADAPTER_PROTOCOL.md](ADAPTER_PROTOCOL.md)：adapter 协议骨架
- [EXTENSION_PROTOCOL.md](EXTENSION_PROTOCOL.md)：extension 协议骨架

### 工具
- [../tools/init_module.py](../tools/init_module.py)：生成新模块骨架
- [../tools/apply_harness.py](../tools/apply_harness.py)：给现有模块补齐 harness 结构
- [../tools/validate_module.py](../tools/validate_module.py)：校验文档、配置和 smoke test

## 扩展面

- `templates/`：默认骨架模板，只提供安全起点
- `profiles/`：轻量规则预设，只描述类型差异
- `adapters/`：适配器层工作区，承接外部接入协议
- `.openclaw_skill/`：OpenClaw skill 镜像版本
- `examples/local_extension/`：项目本地扩展示例

## 版本信息

- 当前版本：`v1.0.1 beta`
- 基线类型：薄核心、强合同、高扩展空间
- 状态：已冻结为独立 beta 基线
- 回滚锚点：`v1.0.0`

## 开发规范入口

这套仓库级规范可以从两条线读取，并且两条线保持一致：

- 文档入口：[`../harness_core/BOUNDARIES.md`](../harness_core/BOUNDARIES.md)
- 程序入口：`harness_core.describe_development_guidance()`

其中：

- `core.py` 说明核心边界怎么冻结
- `markers.py` 说明关键路径、关键变量和关键耦合怎么标记
- `rendering.py` 说明这些标记如何渲染到 `INDEX.md` / `SPEC.md`
- `validate_module.py` 说明这些标记如何被校验
- `describe_extension_guidance()` 说明扩展层怎么保持边界
- `describe_adapter_protocol()` 说明外部接入翻译层的最小协议

## 仍未收口的事项

下面这些属于后续继续补齐的入口，暂时不并入 `core`：

- `adapters/` 下的具体适配器示例
- 更复杂的 OS / 多 agent / 外部项目接入示例
- 更细的 profile pack / template pack 组织方式
- 更完整的 adapter 校验矩阵

这些内容优先保留为说明文档和样例，不先做成厚平台。

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

### 运行示例

```bash
python examples/hello_world/tests/smoke.py
python examples/local_extension/harness/run_harness.py
```

## OpenHarness Bridge

- [OPENHARNESS_BRIDGE.md](OPENHARNESS_BRIDGE.md)
- [OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md](OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md)
- [OPENHARNESS_SDK_BINDING.md](OPENHARNESS_SDK_BINDING.md)
- [OPENHARNESS_EXTERNAL_VERIFY.md](OPENHARNESS_EXTERNAL_VERIFY.md)
- [OPENHARNESS_BRIDGE_OPEN_ITEMS.md](OPENHARNESS_BRIDGE_OPEN_ITEMS.md)
- [OPENHARNESS_BRIDGE_INDEX.md](OPENHARNESS_BRIDGE_INDEX.md)

## OpenHarness 外部复核

- 外部验证目录：`C:/Users/Y2516/Desktop/openharness_app_external_verify`
- 已验证：`@openharness/core@0.6.0` `Agent` 可实例化
- 已验证：`Agent.run(...)` 可用本地 mock model 干跑
- 已验证：`harness_validate` 可通过 process transport 被外部 OpenHarness app 调用
- 已验证：`provider_hints` / `middleware_hints` 仍停留在 bridge 层
