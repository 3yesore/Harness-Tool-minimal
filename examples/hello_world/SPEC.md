# 接口规范: hello_world

## 输入

### 参数
```json
{
  "name": "string"
}
```

### 约束
- `name`: 可选，默认 "World"

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
  "message": "错误描述"
}
```

## 配置

### 配置文件: `configs/default.json`
```json
{
  "greeting": "Hello"
}
```

## 错误处理

- 输入验证失败：返回 `INVALID_INPUT`

## 示例

### Python
```python
from examples.hello_world.src.main import greet

result = greet(name="Alice")
print(result)  # {"status": "success", "message": "Hello, Alice!"}
```

### CLI
```bash
python examples/hello_world/src/main.py --name Alice
```
