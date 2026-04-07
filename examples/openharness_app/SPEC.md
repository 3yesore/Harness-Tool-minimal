# 接口规范: openharness_app

## 调用入口
- `entry_file`: `src/main.py`
- `call_path`: `src/main.py`
- `call_entry`: `src/main.py`

## 输入

### 参数
```json
{
  "module_path": "string",
  "profile": "string",
  "strict": true
}
```

### 约束
- `module_path`: 默认 `examples/local_extension`
- `profile`: 默认 `default`
- `strict`: 默认 `true`

## 输出

### 成功响应
```json
{
  "status": "success",
  "tool_name": "harness_validate",
  "binding_type": "sdk-shell"
}
```

### 错误响应
```json
{
  "status": "error",
  "message": "错误信息"
}
```

## 配置

### 配置文件
- `package.json`
- `tsconfig.json`

## 错误处理

- transport 失败时应返回可解析 JSON
- `npm run smoke` 失败时视为 bridge / binding / transport 失配

## 示例

### Build
```bash
npm run build
```

### Smoke
```bash
npm run smoke
```

## 关键标记
- `entry_file`: `src/main.py`
- `call_path`: `src/main.py`
- `call_entry`: `src/main.py`
