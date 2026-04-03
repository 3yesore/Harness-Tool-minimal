#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hello World 冒烟测试
"""

import sys
import io
from pathlib import Path

# 设置 UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 添加 src 到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from main import greet


def test_default_greeting():
    """测试默认问候"""
    result = greet()
    assert result["status"] == "success"
    assert "World" in result["message"]
    print("[PASS] 默认问候测试通过")


def test_custom_greeting():
    """测试自定义问候"""
    result = greet("Alice")
    assert result["status"] == "success"
    assert "Alice" in result["message"]
    print("[PASS] 自定义问候测试通过")


def test_invalid_input():
    """测试无效输入"""
    result = greet(123)
    assert result["status"] == "error"
    assert result["code"] == "INVALID_INPUT"
    print("[PASS] 无效输入测试通过")


def main():
    print("运行 hello_world 冒烟测试...\n")
    
    try:
        test_default_greeting()
        test_custom_greeting()
        test_invalid_input()
        
        print("\n[SUCCESS] 所有测试通过")
        return 0
    except AssertionError as e:
        print(f"\n[FAIL] 测试失败: {e}")
        return 1
    except Exception as e:
        print(f"\n[ERROR] 运行错误: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
