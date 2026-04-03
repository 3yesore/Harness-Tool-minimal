#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证模块是否符合 Harness 规范。

Usage:
    python validate_module.py <module_path> [--strict] [--profile <profile_name>]
"""

import argparse
import io
import json
import re
import subprocess
import sys
from pathlib import Path


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent.parent
PROFILES_DIR = ROOT_DIR / "profiles"


def load_profile_rules(profile_name: str) -> dict:
    """Load profile rules from profiles/<profile>.rules.json."""
    profile_path = PROFILES_DIR / f"{profile_name}.rules.json"
    if not profile_path.exists():
        if profile_name != "default":
            print(f"[WARN] 未找到 profile: {profile_name}，回退到 default")
        profile_path = PROFILES_DIR / "default.rules.json"

    try:
        return json.loads(profile_path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise RuntimeError(f"无法读取 profile 规则文件: {profile_path} ({exc})") from exc


class HarnessValidator:
    """Harness 规范验证器。"""

    def __init__(self, module_path: str, strict: bool = False, profile: str = "default"):
        self.module_path = Path(module_path)
        self.strict = strict
        self.profile = profile
        self.rules = load_profile_rules(profile)
        self.errors = []
        self.warnings = []

    def validate(self) -> bool:
        """执行完整验证。"""
        print(f"验证模块: {self.module_path}")
        print(f"使用 profile: {self.rules.get('profile', self.profile)}\n")

        self._check_required_files()
        self._validate_changelog()

        if (self.module_path / "INDEX.md").exists():
            self._validate_index()

        if (self.module_path / "SPEC.md").exists():
            self._validate_spec()

        self._validate_tests()
        self._run_smoke_test()
        self._validate_configs()
        self._validate_recommended_paths()

        self._print_results()
        return len(self.errors) == 0

    def _check_required_files(self):
        """Check required files from profile rules."""
        required = self.rules.get("required_files", ["INDEX.md", "SPEC.md"])
        for filename in required:
            filepath = self.module_path / filename
            if not filepath.exists():
                self.errors.append(f"缺少必需文件: {filename}")
            else:
                print(f"[OK] 找到 {filename}")

    def _validate_changelog(self):
        """Validate CHANGELOG.md."""
        changelog_path = self.module_path / "CHANGELOG.md"
        if not changelog_path.exists():
            self.warnings.append("建议添加 CHANGELOG.md 记录变更历史")
            return

        print("[OK] 找到 CHANGELOG.md")
        content = changelog_path.read_text(encoding="utf-8")

        if not re.search(r"\[[\d\.]+\]", content):
            self.warnings.append("CHANGELOG.md 建议使用版本号格式 [x.y.z]")

        if not re.search(r"\d{4}-\d{2}-\d{2}", content):
            self.warnings.append("CHANGELOG.md 建议包含日期 (YYYY-MM-DD)")

    def _validate_index(self):
        """Validate INDEX.md."""
        index_path = self.module_path / "INDEX.md"
        content = index_path.read_text(encoding="utf-8")

        required_sections = self.rules.get(
            "required_index_sections",
            ["## 职责", "## 关键文件", "## 依赖", "## 快速验证"],
        )

        for section in required_sections:
            if section not in content:
                self.errors.append(f"INDEX.md 缺少必需章节: {section}")
            else:
                print(f"[OK] INDEX.md 包含 {section}")

        self._validate_key_files(content)
        self._validate_quick_verification(content)

        if "## 维护注意事项" not in content:
            self.warnings.append("INDEX.md 建议添加 '## 维护注意事项' 章节")

    def _validate_key_files(self, index_content: str):
        """Validate key file paths referenced by INDEX.md."""
        key_files_match = re.search(r"## 关键文件\s*\n(.*?)(?=\n##|\Z)", index_content, re.DOTALL)
        if not key_files_match:
            return

        key_files_section = key_files_match.group(1)
        file_paths = re.findall(r"`([^`]+)`", key_files_section)

        checked_count = 0
        for file_path in file_paths:
            if ":" in file_path and not file_path.startswith("/") and not file_path.startswith("."):
                continue

            full_path = self.module_path / file_path
            if not full_path.exists():
                self.warnings.append(f"关键文件不存在: {file_path}")
            else:
                checked_count += 1

        if checked_count > 0:
            print(f"[OK] 验证了 {checked_count} 个关键文件路径")

    def _validate_quick_verification(self, index_content: str):
        """Validate the quick verification command."""
        quick_verify_match = re.search(r"## 快速验证\s*\n(.*?)(?=\n##|\Z)", index_content, re.DOTALL)
        if not quick_verify_match:
            return

        quick_verify_section = quick_verify_match.group(1)
        code_blocks = re.findall(r"```(?:bash|sh|python)?\s*\n(.*?)\n```", quick_verify_section, re.DOTALL)

        if not code_blocks:
            self.warnings.append("快速验证章节未找到可执行命令")
            return

        for code_block in code_blocks:
            commands = re.findall(r"(?:python|bash|sh|\.\/)?\s+([^\s]+\.(?:py|sh))", code_block)
            for cmd_file in commands:
                cmd_file = cmd_file.lstrip("./")
                full_path = self.module_path / cmd_file
                if not full_path.exists():
                    self.warnings.append(f"快速验证命令引用的文件不存在: {cmd_file}")

        print("[OK] 检查了快速验证命令")

    def _validate_spec(self):
        """Validate SPEC.md."""
        spec_path = self.module_path / "SPEC.md"
        content = spec_path.read_text(encoding="utf-8")

        required_sections = self.rules.get(
            "required_spec_sections",
            ["## 输入", "## 输出", "## 配置", "## 错误处理", "## 示例"],
        )

        for section in required_sections:
            if section not in content:
                self.errors.append(f"SPEC.md 缺少必需章节: {section}")
            else:
                print(f"[OK] SPEC.md 包含 {section}")

    def _validate_tests(self):
        """Validate tests directory."""
        tests_dir = self.module_path / "tests"
        if not tests_dir.exists():
            self.errors.append("缺少 tests/ 目录")
            return

        print("[OK] 找到 tests/ 目录")
        test_files = list(tests_dir.glob("*.py"))
        if not test_files:
            self.warnings.append("tests/ 目录为空，建议添加冒烟测试")
        else:
            print(f"[OK] 找到 {len(test_files)} 个测试文件")
            if not (tests_dir / "smoke.py").exists():
                self.warnings.append("tests/ 目录中未找到 smoke.py，建议提供统一的冒烟测试入口")

    def _run_smoke_test(self):
        """Execute tests/smoke.py when available."""
        smoke_test = self.module_path / "tests" / "smoke.py"
        if not smoke_test.exists():
            self.warnings.append("未找到 tests/smoke.py，跳过冒烟测试执行")
            return

        print(f"[RUN] 执行冒烟测试: {smoke_test}")
        try:
            result = subprocess.run(
                [sys.executable, "tests/smoke.py"],
                cwd=self.module_path,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
        except Exception as exc:
            self.errors.append(f"冒烟测试执行失败: {exc}")
            return

        if result.stdout.strip():
            print(result.stdout.rstrip())
        if result.stderr.strip():
            print(result.stderr.rstrip(), file=sys.stderr)

        if result.returncode != 0:
            self.errors.append(f"冒烟测试返回非零退出码: {result.returncode}")
        else:
            print("[OK] 冒烟测试执行通过")

    def _validate_configs(self):
        """Validate JSON configs in configs/."""
        configs_dir = self.module_path / "configs"
        if not configs_dir.exists():
            self.warnings.append("未找到 configs/ 目录（可选）")
            return

        print("[OK] 找到 configs/ 目录")
        for config_file in configs_dir.glob("*.json"):
            try:
                with open(config_file, "r", encoding="utf-8") as f:
                    json.load(f)
                print(f"[OK] {config_file.name} 格式正确")
            except json.JSONDecodeError as exc:
                self.errors.append(f"{config_file.name} JSON 格式错误: {exc}")

    def _validate_recommended_paths(self):
        """Warn when recommended paths from profile are missing."""
        for path_name in self.rules.get("recommended_paths", []):
            if not (self.module_path / path_name).exists():
                self.warnings.append(f"建议补充目录: {path_name}")

        for file_name in self.rules.get("recommended_files", []):
            if not (self.module_path / file_name).exists():
                self.warnings.append(f"建议补充文件: {file_name}")

    def _print_results(self):
        """Print validation summary."""
        print("\n" + "=" * 60)

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

        print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="验证 Harness 模块")
    parser.add_argument("module_path", help="模块路径")
    parser.add_argument("--strict", action="store_true", help="严格模式（警告也视为错误）")
    parser.add_argument("--profile", default="default", help="规则预设名称（默认: default）")

    args = parser.parse_args()

    if not Path(args.module_path).exists():
        print(f"错误: 路径不存在: {args.module_path}")
        sys.exit(1)

    try:
        validator = HarnessValidator(args.module_path, args.strict, args.profile)
    except RuntimeError as exc:
        print(f"错误: {exc}")
        sys.exit(1)

    success = validator.validate()

    if args.strict and validator.warnings:
        success = False

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
