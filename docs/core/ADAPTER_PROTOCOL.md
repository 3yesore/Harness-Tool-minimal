# Harness Tool Adapter Protocol

## 作用
`adapter` 是 core 外层的接入翻译层，负责把外部世界翻译成 `harness_tool` 能理解的标准输入。

## 最小元数据
- `name`
- `version`
- `type`
- `scope`
- `entrypoint`
- `capabilities`
- `protocol_version`
- `required_core_version`

## 最小生命周期
- `discover()`
- `attach()`
- `adapt()`
- `execute()`
- `teardown()`

## 最小输出
- `adapted_context`
- `capability_report`
- `warnings`
- `errors`

## adapter 必须硬的壳
- 协议版本
- 生命周期
- 能力声明
- 兼容版本
- 统一输出

## adapter 可以软的内容
- 外部接入实现方式
- 环境差异处理细节
- 项目自己的辅助脚本
- 进程/文件系统/工作区的具体封装

## adapter 不做的事
- 不裁判模块是否合格
- 不替代 core contract
- 不吞掉 extension 协议
- 不把自己做成厚平台

## 适合的 adapter 类型
- `WorkspaceAdapter`
- `OSAdapter`
- `WorkflowAdapter`
- `AgentAdapter`
- `ProjectAdapter`
