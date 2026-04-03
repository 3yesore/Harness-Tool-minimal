#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户认证模块
"""

import re
import hashlib


def validate_username(username: str) -> bool:
    """验证用户名"""
    if not isinstance(username, str):
        return False
    if len(username) < 3 or len(username) > 20:
        return False
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False
    return True


def validate_password(password: str) -> bool:
    """验证密码强度"""
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    if not re.search(r'[a-zA-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True


def validate_email(email: str) -> bool:
    """验证邮箱格式"""
    if not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def hash_password(password: str) -> str:
    """哈希密码（简化版，生产环境应使用 bcrypt）"""
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    """验证密码"""
    return hash_password(password) == hashed
