# 接口规范: hello_world

## 调用入口
- `entry_file`: `src/main.py`
- `call_path`: `src/main.py`
- `call_entry`: `src/main.py`

## 输入

### 参数
```json
{
  "name": "string"
}
```

### 约束
- `name`: 可选，默认 `"World"`

## 输出

### 成功响应
```json
{
  "status": "success",
  "message": "Hello, {name}!"
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
  "greeting": "Hello"
}
```

## 错误处理

- 输入验证失败时返回 `INVALID_INPUT`

## 示例

### Python
```python
from examples.hello_world.src.main import greet

result = greet(name="Alice")
print(result)
```

### CLI
```bash
python examples/hello_world/src/main.py --name Alice
```

## 关键标记
- `entry_file`: `src/main.py`
- `call_path`: `src/main.py`
- `call_entry`: `src/main.py`
