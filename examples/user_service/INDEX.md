# Module: user_service

## 职责
提供用户注册、认证和基础信息管理功能

## 关键文件
- `src/user_service.py`: 核心服务实现
- `src/auth.py`: 认证逻辑
- `src/errors.py`: 错误定义
- `configs/dev.json`: 开发环境配置
- `configs/prod.json`: 生产环境配置
- `tests/smoke.py`: 冒烟测试

## 依赖
- 外部依赖: 
  - `bcrypt>=4.0.0` (密码哈希)
  - `pyjwt>=2.8.0` (JWT 令牌)
- 内部依赖: 无

## 快速验证
```bash
python tests/smoke.py
```

## 维护注意事项
- 密码必须经过 bcrypt 哈希，不能明文存储
- JWT 密钥从环境变量 `JWT_SECRET` 读取
- 生产环境必须使用 `configs/prod.json`
- 用户名长度限制 3-20 字符
- 认证失败 3 次后锁定账户 15 分钟

## 最后更新
- 日期: 2026-04-03
- 变更: 初始化用户服务模块
