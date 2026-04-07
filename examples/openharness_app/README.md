# OpenHarness App Example

这个示例用于验证两件事：

1. `@openharness/core` 的 `Agent` 能按真实 API 成功实例化
2. `harness_validate` 能通过 `scripts/openharness_validate_transport.py` 被 OpenHarness tool 调到

这个示例不做真实 LLM 调用，不做 provider 或 middleware 深接入，只验证：

- `bridge`
- `sdk binding`
- `process transport`

## 快速使用

```bash
npm install
npm run build
npm run smoke
```

## 结构

- `src/main.py`: 给当前 Harness 合同识别用的 Python shim
- `src/main.ts`: 绑定导出、tool 构造、agent 实例化
- `src/smoke.ts`: 实例化和 transport 验证
- `src/types.ts`: binding/transport 类型
- `tests/smoke.py`: 供 Harness Tool 调用的外层 smoke

## 说明

- 默认消费 `examples/local_extension` 的 binding 与 validate
- 默认使用 `python` 调 transport，可通过 `PYTHON` 环境变量覆盖
- `openai("gpt-5.4")` 只用于实例化 `Agent`，本示例 smoke 不会发真实模型请求
- `src/main.py` 只是合同入口 shim，真实 OpenHarness 示例入口仍然是 `src/main.ts`
