# 接口规范: {{MODULE_NAME}}

## 输入

### 参数
```json
{
  "param1": "string",
  "param2": 123
}
```

### 约束
- `param1`: 必需，非空字符串
- `param2`: 可选，默认 0

## 输出

### 成功响应
```json
{
  "status": "success",
  "data": {}
}
```

### 错误响应
```json
{
  "status": "error",
  "code": "ERROR_CODE",
  "message": "错误描述"
}
```

### 错误码
- `INVALID_INPUT`: 输入参数不合法
- `RUNTIME_ERROR`: 运行时错误

## 配置

### 配置文件: `configs/default.json`
```json
{
  "timeout": 30,
  "retry": 3
}
```

### 环境变量
- `MODULE_ENV`: 运行环境（dev/prod）

## 错误处理

- 输入验证失败：返回 `INVALID_INPUT`
- 运行时异常：记录日志，返回 `RUNTIME_ERROR`
- 超时：自动重试，超过 `retry` 次数后失败

## 示例

### Python
```python
from module_name import run

result = run(param1="value", param2=123)
print(result)
```

### CLI
```bash
python src/main.py --param1 value --param2 123
```
