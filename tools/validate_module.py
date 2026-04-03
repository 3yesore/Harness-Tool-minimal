#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证模块是否符合 Harness 规范

Usage:
    python validate_harness.py <module_path> [--strict]
"""

import os
import sys
import io
import json
import argparse
from pathlib import Path
from typing import List, Dict, Tuple

# 设置 UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class HarnessValidator:
    """Harness 规范验证器"""
    
    def __init__(self, module_path: str, strict: bool = False):
        self.module_path = Path(module_path)
        self.strict = strict
        self.errors = []
        self.warnings = []
        
    def validate(self) -> bool:
        """执行完整验证"""
        print(f"验证模块: {self.module_path}\n")
        
        # 检查必需文件
        self._check_required_files()
        
        # 检查 INDEX.md
        if (self.module_path / "INDEX.md").exists():
            self._validate_index()
        
        # 检查 SPEC.md
        if (self.module_path / "SPEC.md").exists():
            self._validate_spec()
        
        # 检查测试
        self._validate_tests()
        
        # 检查配置
        self._validate_configs()
        
        # 输出结果
        self._print_results()
        
        return len(self.errors) == 0
    
    def _check_required_files(self):
        """检查必需文件"""
        required = ["INDEX.md", "SPEC.md"]
        
        for filename in required:
            filepath = self.module_path / filename
            if not filepath.exists():
                self.errors.append(f"缺少必需文件: {filename}")
            else:
                print(f"[OK] 找到 {filename}")
    
    def _validate_index(self):
        """验证 INDEX.md"""
        index_path = self.module_path / "INDEX.md"
        content = index_path.read_text(encoding="utf-8")
        
        required_sections = [
            "## 职责",
            "## 关键文件",
            "## 依赖",
            "## 快速验证"
        ]
        
        for section in required_sections:
            if section not in content:
                self.errors.append(f"INDEX.md 缺少必需章节: {section}")
            else:
                print(f"[OK] INDEX.md 包含 {section}")
        
        # 检查是否有维护注意事项（推荐但非必需）
        if "## 维护注意事项" not in content:
            self.warnings.append("INDEX.md 建议添加 '## 维护注意事项' 章节")
    
    def _validate_spec(self):
        """验证 SPEC.md"""
        spec_path = self.module_path / "SPEC.md"
        content = spec_path.read_text(encoding="utf-8")
        
        required_sections = [
            "## 输入",
            "## 输出",
            "## 配置",
            "## 错误处理",
            "## 示例"
        ]
        
        for section in required_sections:
            if section not in content:
                self.errors.append(f"SPEC.md 缺少必需章节: {section}")
            else:
                print(f"[OK] SPEC.md 包含 {section}")
    
    def _validate_tests(self):
        """验证测试"""
        tests_dir = self.module_path / "tests"
        
        if not tests_dir.exists():
            self.errors.append("缺少 tests/ 目录")
            return
        
        print(f"[OK] 找到 tests/ 目录")
        
        # 检查是否有测试文件
        test_files = list(tests_dir.glob("*.py"))
        if not test_files:
            self.warnings.append("tests/ 目录为空，建议添加冒烟测试")
        else:
            print(f"[OK] 找到 {len(test_files)} 个测试文件")
    
    def _validate_configs(self):
        """验证配置"""
        configs_dir = self.module_path / "configs"
        
        if not configs_dir.exists():
            self.warnings.append("未找到 configs/ 目录（可选）")
            return
        
        print(f"[OK] 找到 configs/ 目录")
        
        # 检查配置文件格式
        for config_file in configs_dir.glob("*.json"):
            try:
                with open(config_file, "r", encoding="utf-8") as f:
                    json.load(f)
                print(f"[OK] {config_file.name} 格式正确")
            except json.JSONDecodeError as e:
                self.errors.append(f"{config_file.name} JSON 格式错误: {e}")
    
    def _print_results(self):
        """输出验证结果"""
        print("\n" + "="*60)
        
        if self.errors:
            print(f"\n❌ 发现 {len(self.errors)} 个错误:\n")
            for error in self.errors:
                print(f"  - {error}")
        
        if self.warnings:
            print(f"\n⚠️  发现 {len(self.warnings)} 个警告:\n")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        if not self.errors and not self.warnings:
            print("\n[SUCCESS] 验证通过！模块完全符合 Harness 规范。")
        elif not self.errors:
            print("\n[SUCCESS] 验证通过（有警告）。")
        else:
            print("\n[FAIL] 验证失败。")
        
        print("="*60)


def main():
    parser = argparse.ArgumentParser(description="验证 Harness 模块")
    parser.add_argument("module_path", help="模块路径")
    parser.add_argument("--strict", action="store_true", help="严格模式（警告也视为错误）")
    
    args = parser.parse_args()
    
    if not Path(args.module_path).exists():
        print(f"错误: 路径不存在: {args.module_path}")
        sys.exit(1)
    
    validator = HarnessValidator(args.module_path, args.strict)
    success = validator.validate()
    
    if args.strict and validator.warnings:
        success = False
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
