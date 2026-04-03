# 接口规范: user_service

## 输入

### register(username, password, email)
注册新用户

**参数**:
```json
{
  "username": "string",
  "password": "string",
  "email": "string"
}
```

**约束**:
- `username`: 必需，3-20 字符，仅字母数字下划线
- `password`: 必需，最少 8 字符，必须包含字母和数字
- `email`: 必需，有效的邮箱格式

### authenticate(username, password)
用户认证

**参数**:
```json
{
  "username": "string",
  "password": "string"
}
```

**约束**:
- `username`: 必需
- `password`: 必需

## 输出

### 成功响应
```json
{
  "status": "success",
  "data": {
    "user_id": "string",
    "username": "string",
    "token": "string"
  }
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
- `INVALID_USERNAME`: 用户名不符合要求
- `INVALID_PASSWORD`: 密码不符合要求
- `INVALID_EMAIL`: 邮箱格式错误
- `USER_EXISTS`: 用户已存在
- `USER_NOT_FOUND`: 用户不存在
- `AUTH_FAILED`: 认证失败
- `ACCOUNT_LOCKED`: 账户已锁定
- `TOKEN_EXPIRED`: 令牌已过期

## 配置

### 配置文件
- `configs/dev.json`: 开发环境配置
- `configs/prod.json`: 生产环境配置

### 配置项
```json
{
  "db_path": "users.db",
  "jwt_expiry": 3600,
  "max_login_attempts": 3,
  "lockout_duration": 900
}
```

### 环境变量
- `JWT_SECRET`: JWT 签名密钥（必需）
- `ENV`: 环境标识（dev/prod，默认 dev）

## 错误处理

- 输入验证失败: 返回对应的 `INVALID_*` 错误码
- 认证失败: 返回 `AUTH_FAILED`，累计失败次数
- 账户锁定: 返回 `ACCOUNT_LOCKED`，包含解锁时间
- 数据库错误: 记录日志，返回通用错误

## 示例

### Python
```python
from user_service import UserService

service = UserService()

# 注册用户
result = service.register(
    username="alice",
    password="Pass1234",
    email="alice@example.com"
)

if result["status"] == "success":
    print(f"注册成功: {result['data']['user_id']}")

# 认证用户
result = service.authenticate(
    username="alice",
    password="Pass1234"
)

if result["status"] == "success":
    token = result["data"]["token"]
    print(f"认证成功，令牌: {token}")
```

### CLI
```bash
# 设置环境变量
export JWT_SECRET="your-secret-key"
export ENV="dev"

# 运行服务
python src/user_service.py
```
