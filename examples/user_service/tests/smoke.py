#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
user_service 冒烟测试
"""

import sys
import io
from pathlib import Path

# 设置 UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 添加 src 到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from user_service import UserService


def test_register_success():
    """测试成功注册"""
    service = UserService()
    result = service.register("testuser", "Pass1234", "test@example.com")
    
    assert result["status"] == "success", f"注册失败: {result}"
    assert "user_id" in result["data"]
    assert result["data"]["username"] == "testuser"
    
    print("[PASS] 用户注册测试通过")


def test_register_invalid_username():
    """测试无效用户名"""
    service = UserService()
    result = service.register("ab", "Pass1234", "test@example.com")  # 太短
    
    assert result["status"] == "error"
    assert result["code"] == "INVALID_USERNAME"
    
    print("[PASS] 无效用户名测试通过")


def test_register_invalid_password():
    """测试无效密码"""
    service = UserService()
    result = service.register("testuser", "weak", "test@example.com")  # 太弱
    
    assert result["status"] == "error"
    assert result["code"] == "INVALID_PASSWORD"
    
    print("[PASS] 无效密码测试通过")


def test_authenticate_success():
    """测试成功认证"""
    service = UserService()
    
    # 先注册
    service.register("alice", "Pass1234", "alice@example.com")
    
    # 再认证
    result = service.authenticate("alice", "Pass1234")
    
    assert result["status"] == "success"
    assert "token" in result["data"]
    
    print("[PASS] 用户认证测试通过")


def test_authenticate_wrong_password():
    """测试错误密码"""
    service = UserService()
    
    # 先注册
    service.register("bob", "Pass1234", "bob@example.com")
    
    # 错误密码
    result = service.authenticate("bob", "WrongPass")
    
    assert result["status"] == "error"
    assert result["code"] == "AUTH_FAILED"
    
    print("[PASS] 错误密码测试通过")


def test_account_lockout():
    """测试账户锁定"""
    service = UserService()
    
    # 先注册
    service.register("charlie", "Pass1234", "charlie@example.com")
    
    # 连续失败 3 次
    for _ in range(3):
        service.authenticate("charlie", "WrongPass")
    
    # 第 4 次应该被锁定
    result = service.authenticate("charlie", "Pass1234")
    
    assert result["status"] == "error"
    assert result["code"] == "ACCOUNT_LOCKED"
    
    print("[PASS] 账户锁定测试通过")


def main():
    print("运行 user_service 冒烟测试...\n")
    
    try:
        test_register_success()
        test_register_invalid_username()
        test_register_invalid_password()
        test_authenticate_success()
        test_authenticate_wrong_password()
        test_account_lockout()
        
        print("\n[SUCCESS] 所有测试通过")
        return 0
    except AssertionError as e:
        print(f"\n[FAIL] 测试失败: {e}")
        return 1
    except Exception as e:
        print(f"\n[ERROR] 运行错误: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
