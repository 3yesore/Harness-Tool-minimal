# Module: openharness_app

## 职责
验证 `harness_tool` 与 OpenHarness 的窄桥接入路径。

## 关键文件
- `src/main.py`: Harness 合同侧 shim，指向 TypeScript 示例
- `src/main.ts`: OpenHarness Agent 实例和 binding 消费入口
- `src/smoke.ts`: transport 和实例化验证
- `tests/smoke.py`: Harness Tool 冒烟测试入口
- `package.json`: npm 依赖和脚本定义

## 调用入口
- `module_name`: `openharness_app`
- `entry_file`: `src/main.py`
- `call_path`: `src/main.py`
- `call_entry`: `src/main.py`

## 关键标记
- `entry_file`: `src/main.py`
- `call_path`: `src/main.py`
- `call_entry`: `src/main.py`

## 依赖
- 外部依赖: `@openharness/core`, `@ai-sdk/openai`, `ai`, `zod`
- 内部依赖: `adapters/openharness_bridge.py`, `adapters/openharness_sdk_binding.py`, `scripts/openharness_validate_transport.py`

## 快速验证
```bash
npm run build
npm run smoke
python tests/smoke.py
```

## 维护注意事项
- 这里只验证安装、实例化和 transport，不宿主 OpenHarness runtime。
- 不要把 provider、middleware、session 逻辑移入 `harness_core`。
- 默认目标模块是 `examples/local_extension`。

## 变更记录
- 日期: 2026-04-07
- 说明: 增加最小 OpenHarness app 验证示例
