#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户服务核心实现
"""

import json
import os
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, Any

# 直接导入，避免相对导入
import sys
sys.path.insert(0, str(Path(__file__).parent))

from errors import (
    InvalidUsernameError,
    InvalidPasswordError,
    InvalidEmailError,
    UserExistsError,
    UserNotFoundError,
    AuthFailedError,
    AccountLockedError,
)
from auth import (
    validate_username,
    validate_password,
    validate_email,
    hash_password,
    verify_password,
)


class UserService:
    """用户服务"""
    
    def __init__(self, config_path: str = None):
        """初始化用户服务"""
        if config_path is None:
            env = os.getenv("ENV", "dev")
            config_path = Path(__file__).parent.parent / "configs" / f"{env}.json"
        
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        
        self.users = {}  # 简化版，生产环境应使用数据库
        self.login_attempts = {}  # 登录尝试记录
    
    def register(self, username: str, password: str, email: str) -> Dict[str, Any]:
        """注册用户"""
        try:
            # 验证输入
            if not validate_username(username):
                raise InvalidUsernameError()
            if not validate_password(password):
                raise InvalidPasswordError()
            if not validate_email(email):
                raise InvalidEmailError()
            
            # 检查用户是否存在
            if username in self.users:
                raise UserExistsError()
            
            # 创建用户
            user_id = f"user_{len(self.users) + 1}"
            self.users[username] = {
                "user_id": user_id,
                "username": username,
                "password_hash": hash_password(password),
                "email": email,
                "created_at": datetime.now().isoformat(),
            }
            
            return {
                "status": "success",
                "data": {
                    "user_id": user_id,
                    "username": username,
                }
            }
        
        except (InvalidUsernameError, InvalidPasswordError, InvalidEmailError, UserExistsError) as e:
            return {
                "status": "error",
                "code": e.code,
                "message": e.message,
            }
    
    def authenticate(self, username: str, password: str) -> Dict[str, Any]:
        """认证用户"""
        try:
            # 检查账户锁定
            if username in self.login_attempts:
                attempts = self.login_attempts[username]
                if attempts["count"] >= self.config["max_login_attempts"]:
                    lockout_until = attempts["locked_until"]
                    if datetime.now() < lockout_until:
                        raise AccountLockedError(
                            f"账户已锁定至 {lockout_until.strftime('%H:%M:%S')}"
                        )
                    else:
                        # 解锁
                        del self.login_attempts[username]
            
            # 检查用户是否存在
            if username not in self.users:
                raise UserNotFoundError()
            
            user = self.users[username]
            
            # 验证密码
            if not verify_password(password, user["password_hash"]):
                # 记录失败尝试
                if username not in self.login_attempts:
                    self.login_attempts[username] = {"count": 0}
                
                self.login_attempts[username]["count"] += 1
                
                if self.login_attempts[username]["count"] >= self.config["max_login_attempts"]:
                    lockout_duration = self.config["lockout_duration"]
                    self.login_attempts[username]["locked_until"] = (
                        datetime.now() + timedelta(seconds=lockout_duration)
                    )
                
                raise AuthFailedError()
            
            # 认证成功，清除失败记录
            if username in self.login_attempts:
                del self.login_attempts[username]
            
            # 生成令牌（简化版）
            token = f"token_{user['user_id']}_{datetime.now().timestamp()}"
            
            return {
                "status": "success",
                "data": {
                    "user_id": user["user_id"],
                    "username": username,
                    "token": token,
                }
            }
        
        except (UserNotFoundError, AuthFailedError, AccountLockedError) as e:
            return {
                "status": "error",
                "code": e.code,
                "message": e.message,
            }


if __name__ == "__main__":
    # 简单的 CLI 演示
    service = UserService()
    
    # 注册用户
    result = service.register("alice", "Pass1234", "alice@example.com")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # 认证用户
    result = service.authenticate("alice", "Pass1234")
    print(json.dumps(result, ensure_ascii=False, indent=2))
