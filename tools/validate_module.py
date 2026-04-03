#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证模块是否符合 Harness 规范

Usage:
    python validate_module.py <module_path> [--strict]
"""

import os
import sys
import io
import json
import re
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
        
        # 检查 CHANGELOG.md
        self._validate_changelog()
        
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
    
    def _validate_changelog(self):
        """验证 CHANGELOG.md"""
        changelog_path = self.module_path / "CHANGELOG.md"
        
        if not changelog_path.exists():
            self.warnings.append("建议添加 CHANGELOG.md 记录变更历史")
            return
        
        print(f"[OK] 找到 CHANGELOG.md")
        
        content = changelog_path.read_text(encoding="utf-8")
        
        # 检查是否有版本号
        if not re.search(r'\[[\d\.]+\]', content):
            self.warnings.append("CHANGELOG.md 建议使用版本号格式 [x.y.z]")
        
        # 检查是否有日期
        if not re.search(r'\d{4}-\d{2}-\d{2}', content):
            self.warnings.append("CHANGELOG.md 建议包含日期 (YYYY-MM-DD)")
    
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
        
        # 检查关键文件路径是否存在
        self._validate_key_files(content)
        
        # 检查快速验证命令
        self._validate_quick_verification(content)
        
        # 检查是否有维护注意事项（推荐但非必需）
        if "## 维护注意事项" not in content:
            self.warnings.append("INDEX.md 建议添加 '## 维护注意事项' 章节")
    
    def _validate_key_files(self, index_content: str):
        """验证关键文件路径是否存在"""
        # 提取关键文件章节
        key_files_match = re.search(r'## 关键文件\s*\n(.*?)(?=\n##|\Z)', index_content, re.DOTALL)
        if not key_files_match:
            return
        
        key_files_section = key_files_match.group(1)
        
        # 提取文件路径 (匹配 `path/to/file` 格式)
        file_paths = re.findall(r'`([^`]+)`', key_files_section)
        
        checked_count = 0
        for file_path in file_paths:
            # 跳过明显不是路径的内容
            if ':' in file_path and not file_path.startswith('/') and not file_path.startswith('.'):
                continue
            
            full_path = self.module_path / file_path
            if not full_path.exists():
                self.warnings.append(f"关键文件不存在: {file_path}")
            else:
                checked_count += 1
        
        if checked_count > 0:
            print(f"[OK] 验证了 {checked_count} 个关键文件路径")
    
    def _validate_quick_verification(self, index_content: str):
        """验证快速验证命令"""
        # 提取快速验证章节
        quick_verify_match = re.search(r'## 快速验证\s*\n(.*?)(?=\n##|\Z)', index_content, re.DOTALL)
        if not quick_verify_match:
            return
        
        quick_verify_section = quick_verify_match.group(1)
        
        # 提取代码块中的命令
        code_blocks = re.findall(r'```(?:bash|sh|python)?\s*\n(.*?)\n```', quick_verify_section, re.DOTALL)
        
        if not code_blocks:
            self.warnings.append("快速验证章节未找到可执行命令")
            return
        
        # 检查命令中引用的文件是否存在
        for code_block in code_blocks:
            # 提取 python xxx.py 或 ./xxx.sh 等命令
            commands = re.findall(r'(?:python|bash|sh|\./)?\s+([^\s]+\.(?:py|sh))', code_block)
            
            for cmd_file in commands:
                # 移除可能的路径前缀
                cmd_file = cmd_file.lstrip('./')
                full_path = self.module_path / cmd_file
                
                if not full_path.exists():
                    self.warnings.append(f"快速验证命令引用的文件不存在: {cmd_file}")
        
        print(f"[OK] 检查了快速验证命令")
    
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
            print(f"\n[ERROR] 发现 {len(self.errors)} 个错误:\n")
            for error in self.errors:
                print(f"  - {error}")
        
        if self.warnings:
            print(f"\n[WARN] 发现 {len(self.warnings)} 个警告:\n")
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
