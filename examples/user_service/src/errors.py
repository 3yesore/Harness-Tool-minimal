#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户服务错误定义
"""


class UserServiceError(Exception):
    """用户服务基础错误"""
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(message)


class InvalidUsernameError(UserServiceError):
    """用户名不合法"""
    def __init__(self, message="用户名不符合要求"):
        super().__init__("INVALID_USERNAME", message)


class InvalidPasswordError(UserServiceError):
    """密码不合法"""
    def __init__(self, message="密码不符合要求"):
        super().__init__("INVALID_PASSWORD", message)


class InvalidEmailError(UserServiceError):
    """邮箱不合法"""
    def __init__(self, message="邮箱格式错误"):
        super().__init__("INVALID_EMAIL", message)


class UserExistsError(UserServiceError):
    """用户已存在"""
    def __init__(self, message="用户已存在"):
        super().__init__("USER_EXISTS", message)


class UserNotFoundError(UserServiceError):
    """用户不存在"""
    def __init__(self, message="用户不存在"):
        super().__init__("USER_NOT_FOUND", message)


class AuthFailedError(UserServiceError):
    """认证失败"""
    def __init__(self, message="认证失败"):
        super().__init__("AUTH_FAILED", message)


class AccountLockedError(UserServiceError):
    """账户已锁定"""
    def __init__(self, message="账户已锁定"):
        super().__init__("ACCOUNT_LOCKED", message)
