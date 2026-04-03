#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为现有模块半自动补充 Harness 规范文件

Usage:
    python apply_harness.py <module_path> [--interactive]
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


class HarnessApplier:
    """Harness 规范应用器"""
    
    def __init__(self, module_path: str, interactive: bool = True):
        self.module_path = Path(module_path)
        self.interactive = interactive
        self.module_name = self.module_path.name
        
    def apply(self):
        """应用 Harness 规范"""
        print(f"为模块应用 Harness 规范: {self.module_path}\n")
        
        if not self.module_path.exists():
            print(f"[ERROR] 模块路径不存在: {self.module_path}")
            return False
        
        # 分析现有结构
        structure = self._analyze_structure()
        
        # 生成 INDEX.md
        if not (self.module_path / "INDEX.md").exists():
            self._generate_index(structure)
        else:
            print("[SKIP] INDEX.md 已存在")
        
        # 生成 SPEC.md
        if not (self.module_path / "SPEC.md").exists():
            self._generate_spec(structure)
        else:
            print("[SKIP] SPEC.md 已存在")
        
        # 生成 CHANGELOG.md
        if not (self.module_path / "CHANGELOG.md").exists():
            self._generate_changelog()
        else:
            print("[SKIP] CHANGELOG.md 已存在")
        
        # 创建 tests 目录（如果不存在）
        if not (self.module_path / "tests").exists():
            self._create_tests_dir()
        
        print("\n[SUCCESS] Harness 规范应用完成！")
        print("\n下一步:")
        print("  1. 编辑 INDEX.md 补充模块职责和依赖")
        print("  2. 编辑 SPEC.md 定义实际的输入输出")
        print("  3. 添加冒烟测试到 tests/")
        print(f"  4. 运行验证: python tools/validate_module.py {self.module_path}")
        
        return True
    
    def _analyze_structure(self):
        """分析现有模块结构"""
        structure = {
            "has_src": (self.module_path / "src").exists(),
            "has_tests": (self.module_path / "tests").exists(),
            "has_configs": (self.module_path / "configs").exists(),
            "has_docs": (self.module_path / "docs").exists(),
            "python_files": [],
            "config_files": [],
            "test_files": []
        }
        
        # 查找 Python 文件
        for py_file in self.module_path.rglob("*.py"):
            rel_path = py_file.relative_to(self.module_path)
            if "test" in str(rel_path).lower():
                structure["test_files"].append(str(rel_path))
            else:
                structure["python_files"].append(str(rel_path))
        
        # 查找配置文件
        for config_file in self.module_path.rglob("*.json"):
            structure["config_files"].append(str(config_file.relative_to(self.module_path)))
        
        for config_file in self.module_path.rglob("*.yaml"):
            structure["config_files"].append(str(config_file.relative_to(self.module_path)))
        
        for config_file in self.module_path.rglob("*.yml"):
            structure["config_files"].append(str(config_file.relative_to(self.module_path)))
        
        return structure
    
    def _generate_index(self, structure):
        """生成 INDEX.md"""
        print("[CREATE] 生成 INDEX.md...")
        
        # 确定入口文件
        entry_file = "src/main.py" if structure["has_src"] else "main.py"
        if structure["python_files"]:
            # 优先选择 main.py 或第一个 Python 文件
            for py_file in structure["python_files"]:
                if "main" in py_file.lower():
                    entry_file = py_file
                    break
            else:
                entry_file = structure["python_files"][0]
        
        # 确定配置文件
        config_file = "configs/default.json" if structure["has_configs"] else "config.json"
        if structure["config_files"]:
            config_file = structure["config_files"][0]
        
        # 确定测试文件
        test_file = "tests/smoke.py" if structure["has_tests"] else "test.py"
        if structure["test_files"]:
            test_file = structure["test_files"][0]
        
        content = f"""# Module: {self.module_name}

## 职责
[TODO: 一句话说明模块做什么]

## 关键文件
- `{entry_file}`: 入口
- `{config_file}`: 配置
- `{test_file}`: 测试

## 依赖
- 外部依赖: [TODO: 列出 pip/npm 包]
- 内部依赖: [TODO: 列出其他模块]

## 快速验证
```bash
python {test_file}
```

## 维护注意事项
[TODO: 列出关键约束、已知问题、特殊配置等]

## 最后更新
- 日期: {datetime.now().strftime('%Y-%m-%d')}
- 变更: 应用 Harness 规范
"""
        
        index_path = self.module_path / "INDEX.md"
        index_path.write_text(content, encoding="utf-8")
        print(f"[OK] 已创建 {index_path}")
    
    def _generate_spec(self, structure):
        """生成 SPEC.md"""
        print("[CREATE] 生成 SPEC.md...")
        
        content = f"""# 接口规范: {self.module_name}

## 输入

### 参数
```json
{{
  "param1": "string",
  "param2": 123
}}
```

### 约束
- `param1`: [TODO: 描述参数约束]
- `param2`: [TODO: 描述参数约束]

## 输出

### 成功响应
```json
{{
  "status": "success",
  "data": {{}}
}}
```

### 错误响应
```json
{{
  "status": "error",
  "code": "ERROR_CODE",
  "message": "错误描述"
}}
```

### 错误码
- `INVALID_INPUT`: 输入参数不合法
- `RUNTIME_ERROR`: 运行时错误

## 配置

### 配置文件
[TODO: 列出配置文件路径和格式]

### 环境变量
[TODO: 列出需要的环境变量]

## 错误处理

- 输入验证失败: 返回 `INVALID_INPUT`
- 运行时异常: 记录日志,返回 `RUNTIME_ERROR`

## 示例

### Python
```python
# TODO: 添加实际调用示例
from {self.module_name} import run

result = run(param1="value")
print(result)
```

### CLI
```bash
# TODO: 添加命令行示例
python src/main.py --param1 value
```
"""
        
        spec_path = self.module_path / "SPEC.md"
        spec_path.write_text(content, encoding="utf-8")
        print(f"[OK] 已创建 {spec_path}")
    
    def _generate_changelog(self):
        """生成 CHANGELOG.md"""
        print("[CREATE] 生成 CHANGELOG.md...")
        
        content = f"""# Changelog: {self.module_name}

## [Unreleased]

## [1.0.0] - {datetime.now().strftime('%Y-%m-%d')}
### Added
- 应用 Harness 规范
- 添加 INDEX.md 和 SPEC.md

### Changed
- N/A

### Fixed
- N/A

### Removed
- N/A

---

## 变更记录规范

每次变更必须记录:
- 日期
- 变更类型 (Added/Changed/Fixed/Removed)
- 简要描述
- 影响范围 (如果涉及接口变更)
"""
        
        changelog_path = self.module_path / "CHANGELOG.md"
        changelog_path.write_text(content, encoding="utf-8")
        print(f"[OK] 已创建 {changelog_path}")
    
    def _create_tests_dir(self):
        """创建 tests 目录"""
        print("[CREATE] 创建 tests/ 目录...")
        
        tests_dir = self.module_path / "tests"
        tests_dir.mkdir(exist_ok=True)
        
        # 创建示例测试文件
        smoke_test = tests_dir / "smoke.py"
        content = f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
{self.module_name} 冒烟测试
\"\"\"

import sys
import io
from pathlib import Path

# 设置 UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# TODO: 添加实际测试


def test_basic():
    \"\"\"基础功能测试\"\"\"
    # TODO: 实现测试逻辑
    print("[PASS] 基础功能测试通过")


def main():
    print("运行 {self.module_name} 冒烟测试...\\n")
    
    try:
        test_basic()
        
        print("\\n[SUCCESS] 所有测试通过")
        return 0
    except AssertionError as e:
        print(f"\\n[FAIL] 测试失败: {{e}}")
        return 1
    except Exception as e:
        print(f"\\n[ERROR] 运行错误: {{e}}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
"""
        
        smoke_test.write_text(content, encoding="utf-8")
        print(f"[OK] 已创建 {smoke_test}")


def main():
    parser = argparse.ArgumentParser(description="为现有模块应用 Harness 规范")
    parser.add_argument("module_path", help="模块路径")
    parser.add_argument("--interactive", action="store_true", help="交互模式（暂未实现）")
    
    args = parser.parse_args()
    
    applier = HarnessApplier(args.module_path, args.interactive)
    success = applier.apply()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
