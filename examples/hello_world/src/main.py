#!/usr/bin/env python3
"""
Hello World 示例模块
"""

import json
import argparse
from pathlib import Path


def load_config():
    """加载配置"""
    config_path = Path(__file__).parent.parent / "configs" / "default.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def greet(name: str = "World") -> dict:
    """
    生成问候消息
    
    Args:
        name: 要问候的名字
        
    Returns:
        包含 status 和 message 的字典
    """
    if not isinstance(name, str):
        return {
            "status": "error",
            "code": "INVALID_INPUT",
            "message": "name must be a string"
        }
    
    config = load_config()
    greeting = config.get("greeting", "Hello")
    
    return {
        "status": "success",
        "message": f"{greeting}, {name}!"
    }


def main():
    parser = argparse.ArgumentParser(description="Hello World 示例")
    parser.add_argument("--name", default="World", help="要问候的名字")
    
    args = parser.parse_args()
    result = greet(args.name)
    
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
