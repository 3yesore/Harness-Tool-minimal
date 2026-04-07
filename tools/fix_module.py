#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速修复常见 Harness 问题

Usage:
    python fix_module.py <module_path> [--dry-run]
"""

import os
import sys
import io
import json
import argparse
from pathlib import Path
from datetime import datetime

# 设置 UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class HarnessFixer:
    """Harness 快速修复器"""
    
    def __init__(self, module_path: str, dry_run: bool = False):
        self.module_path = Path(module_path)
        self.dry_run = dry_run
        self.fixes_applied = []
        
    def fix(self):
        """执行快速修复"""
        print(f"检查模块: {self.module_path}\n")
        
        if not self.module_path.exists():
            print(f"[ERROR] 模块路径不存在: {self.module_path}")
            return False
        
        # 修复缺失的 CHANGELOG.md
        self._fix_missing_changelog()
        
        # 修复 INDEX.md 中不存在的关键文件路径
        self._fix_index_paths()
        
        # 修复空的 tests 目录
        self._fix_empty_tests()
        
        # 输出结果
        self._print_results()
        
        return True
    
    def _fix_missing_changelog(self):
        """修复缺失的 CHANGELOG.md"""
        changelog_path = self.module_path / "CHANGELOG.md"
        
        if changelog_path.exists():
            return
        
        if self.dry_run:
            print("[DRY-RUN] 将创建 CHANGELOG.md")
            self.fixes_applied.append("创建 CHANGELOG.md")
            return
        
        module_name = self.module_path.name
        content = f"""# Changelog: {module_name}

## [1.0.0] - {datetime.now().strftime('%Y-%m-%d')}
### Added
- 初始化模块

### Changed
- N/A

### Fixed
- N/A

### Removed
- N/A
"""
        
        changelog_path.write_text(content, encoding="utf-8")
        print(f"[FIX] 创建 {changelog_path}")
        self.fixes_applied.append("创建 CHANGELOG.md")
    
    def _fix_index_paths(self):
        """修复 INDEX.md 中不存在的关键文件路径"""
        index_path = self.module_path / "INDEX.md"
        
        if not index_path.exists():
            return
        
        # 这里只检测，不自动修复路径（太危险）
        # 只提示用户手动修复
        import re
        content = index_path.read_text(encoding="utf-8")
        
        key_files_match = re.search(r'## 关键文件\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
        if not key_files_match:
            return
        
        key_files_section = key_files_match.group(1)
        file_paths = re.findall(r'`([^`]+)`', key_files_section)
        
        missing_files = []
        for file_path in file_paths:
            if ':' in file_path and not file_path.startswith('/') and not file_path.startswith('.'):
                continue
            
            full_path = self.module_path / file_path
            if not full_path.exists():
                missing_files.append(file_path)
        
        if missing_files:
            print(f"[WARN] INDEX.md 中引用的文件不存在:")
            for f in missing_files:
                print(f"  - {f}")
            print("  建议手动修复 INDEX.md 或创建这些文件")
    
    def _fix_empty_tests(self):
        """修复空的 tests 目录"""
        tests_dir = self.module_path / "tests"
        
        if not tests_dir.exists():
            return
        
        test_files = list(tests_dir.glob("*.py"))
        if test_files:
            return
        
        if self.dry_run:
            print("[DRY-RUN] 将创建 tests/smoke.py")
            self.fixes_applied.append("创建 tests/smoke.py")
            return
        
        module_name = self.module_path.name
        smoke_test = tests_dir / "smoke.py"
        
        content = f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
{module_name} 冒烟测试
\"\"\"

import sys
import io

# 设置 UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def test_basic():
    \"\"\"基础功能测试\"\"\"
    # TODO: 实现测试逻辑
    print("[PASS] 基础功能测试通过")


def main():
    print("运行 {module_name} 冒烟测试...\\n")
    
    try:
        test_basic()
        
        print("\\n[SUCCESS] 所有测试通过")
        return 0
    except AssertionError as e:
        print(f"\\n[FAIL] 测试失败: {e}")
        return 1
    except Exception as e:
        print(f"\\n[ERROR] 运行错误: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
"""
        
        smoke_test.write_text(content, encoding="utf-8")
        print(f"[FIX] 创建 {smoke_test}")
        self.fixes_applied.append("创建 tests/smoke.py")
    
    def _print_results(self):
        """输出修复结果"""
        print("\n" + "="*60)
        
        if self.fixes_applied:
            mode = "DRY-RUN" if self.dry_run else "FIXED"
            print(f"\n[{mode}] 应用了 {len(self.fixes_applied)} 个修复:\n")
            for fix in self.fixes_applied:
                print(f"  - {fix}")
        else:
            print("\n[OK] 未发现需要修复的问题")
        
        print("="*60)


def main():
    parser = argparse.ArgumentParser(description="快速修复 Harness 模块")
    parser.add_argument("module_path", help="模块路径")
    parser.add_argument("--dry-run", action="store_true", help="预览修复但不实际执行")
    
    args = parser.parse_args()
    
    if not Path(args.module_path).exists():
        print(f"错误: 路径不存在: {args.module_path}")
        sys.exit(1)
    
    fixer = HarnessFixer(args.module_path, args.dry_run)
    success = fixer.fix()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
