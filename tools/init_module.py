#!/usr/bin/env python3
"""
初始化新模块的脚本

Usage:
    python tools/init_module.py <module_name> [--path <output_dir>]
"""

import io
import sys
import argparse
from datetime import datetime
from pathlib import Path


# 设置 UTF-8 输出，避免 Windows 默认编码导致的 Unicode 报错
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def init_module(module_name: str, output_dir: str = "modules"):
    """初始化新模块"""

    module_path = Path(output_dir) / module_name
    if module_path.exists():
        print(f"错误: 模块 {module_name} 已存在于 {output_dir}")
        return False

    dirs = [
        module_path,
        module_path / "src",
        module_path / "tests",
        module_path / "configs",
        module_path / "docs",
    ]

    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

    template_dir = Path(__file__).parent.parent / "templates"
    templates = {
        "INDEX.md": template_dir / "INDEX.md.template",
        "SPEC.md": template_dir / "SPEC.md.template",
        "CHANGELOG.md": template_dir / "CHANGELOG.md.template",
    }

    replacements = {
        "{{MODULE_NAME}}": module_name,
        "{{DATE}}": datetime.now().strftime("%Y-%m-%d"),
    }

    for filename, template_path in templates.items():
        if not template_path.exists():
            print(f"警告: 模板文件 {template_path} 不存在，跳过")
            continue

        content = template_path.read_text(encoding="utf-8")
        for key, value in replacements.items():
            content = content.replace(key, value)

        output_path = module_path / filename
        output_path.write_text(content, encoding="utf-8")
        print(f"[OK] 创建 {output_path}")

    placeholders = {
        "src/main.py": "# TODO: 实现模块入口\n",
        "tests/smoke.py": "# TODO: 实现冒烟测试\n",
        "configs/default.json": "{\n  \"timeout\": 30\n}\n",
    }

    for filepath, content in placeholders.items():
        output_path = module_path / filepath
        output_path.write_text(content, encoding="utf-8")
        print(f"[OK] 创建 {output_path}")

    print(f"\n[OK] 模块 {module_name} 初始化完成: {module_path}")
    print("\n下一步:")
    print(f"  1. 编辑 {module_path}/INDEX.md 和 SPEC.md")
    print(f"  2. 实现 {module_path}/src/main.py")
    print(f"  3. 添加测试 {module_path}/tests/smoke.py")
    print(f"  4. 更新主索引 INDEX.md")

    return True


def main():
    parser = argparse.ArgumentParser(description="初始化新模块")
    parser.add_argument("module_name", help="模块名称")
    parser.add_argument("--path", default="modules", help="输出目录（默认: modules）")

    args = parser.parse_args()

    success = init_module(args.module_name, args.path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
