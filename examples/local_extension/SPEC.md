# 接口规范: local_extension

## 调用入口
- `entry_file`: `src/main.py`
- `call_path`: `harness/run_harness.py`
- `call_entry`: `src/main.py`

## Adapter Envelope
- `ADAPTER_PROTOCOL.md`
- `adapters/protocol.py`
- `adapters/workspace.py`
- `adapters/workflow.py`

## 输入

### 参数
```json
{
  "name": "string"
}
```

### 约束
- `name`: 可选，默认 `"local-extension"`

## 输出

### 成功响应
```json
{
  "status": "success",
  "message": "local extension is ready"
}
```

### 错误响应
```json
{
  "status": "error",
  "code": "INVALID_INPUT",
  "message": "错误信息"
}
```

### 错误码
- `INVALID_INPUT`: 输入参数不合法

## 配置

### 配置文件: `configs/default.json`
```json
{
  "timeout": 30,
  "mode": "local"
}
```

## 错误处理

- 输入验证失败时返回 `INVALID_INPUT`

## 示例

### Python
```python
from src.main import run

result = run()
print(result)
```

### CLI
```bash
python harness/run_harness.py
```

## 关键标记
- `entry_file`: `src/main.py`
- `call_path`: `harness/run_harness.py`
- `call_entry`: `src/main.py`
