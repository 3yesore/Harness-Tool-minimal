# Module: {{MODULE_NAME}}

## 职责
[一句话说明模块做什么]

## 关键文件
- `{{ENTRY_FILE}}`: 入口
- `configs/default.json`: 默认配置
- `tests/smoke.py`: 冒烟测试

## 调用入口
- `module_name`: `{{MODULE_NAME}}`
- `entry_file`: `{{ENTRY_FILE}}`
- `call_path`: `{{CALL_PATH}}`
- `call_entry`: `{{CALL_ENTRY}}`

## 关键标记
- `entry_file`: `{{ENTRY_FILE}}`
- `call_path`: `{{CALL_PATH}}`
- `call_entry`: `{{CALL_ENTRY}}`
- `smoke_test`: `tests/smoke.py`
- `config`: `configs/default.json`

## 依赖
- 外部依赖: [列出 pip/npm 包]
- 内部依赖: [列出相关模块]

## 快速验证
```bash
python tests/smoke.py
```

## 维护注意事项
[列出关键约束、已知问题、部署要点]

## 变更记录
- 日期: {{DATE}}
- 说明: 初始化模块
