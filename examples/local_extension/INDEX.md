# Module: local_extension

## 职责
展示项目本地扩展如何自持规则，并且不进入 `harness_core` 运行时。

## 关键文件
- `harness/run_harness.py`: 项目本地 wrapper
- `harness/extensions/entry_consistency.py`: 本地入口一致性规则
- `harness/extensions/marker_rules.py`: 本地关键标记规则
- `ADAPTER_PROTOCOL.md`: 模块内 adapter envelope 说明
- `adapters/protocol.py`: 模块内 adapter 协议壳
- `adapters/workspace.py`: 模块内 workspace adapter 示例
- `adapters/workflow.py`: 模块内 workflow adapter 示例
- `src/main.py`: 业务入口
- `tests/smoke.py`: 冒烟测试
- `configs/default.json`: 默认配置

## 调用入口
- `module_name`: `local_extension`
- `entry_file`: `src/main.py`
- `call_path`: `harness/run_harness.py`
- `call_entry`: `src/main.py`

## 关键标记
- `entry_file`: `src/main.py`
- `call_path`: `harness/run_harness.py`
- `call_entry`: `src/main.py`
- `smoke_test`: `tests/smoke.py`
- `config`: `configs/default.json`
- `marker_source`: `harness/extensions/marker_rules.py`
- `adapter_protocol`: `ADAPTER_PROTOCOL.md`
- `adapter_entry`: `adapters/protocol.py`

## 依赖
- 外部依赖: 无
- 内部依赖: 无

## 快速验证
```bash
python tests/smoke.py
python harness/run_harness.py
```

## 维护注意事项
- 这是项目本地扩展示例，不要把扩展运行逻辑挪入 `harness_core`。
- 如果需要更细规则，应继续在项目本地扩展目录实现。

## 变更记录
- 日期: 2026-04-07
- 说明: 补入本地扩展示例和 adapter 协议文件
