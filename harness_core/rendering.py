"""Document and scaffold rendering helpers."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Mapping

from .markers import render_marker_section


def _repo_root(root_dir: Path | None = None) -> Path:
    return Path(root_dir) if root_dir is not None else Path(__file__).resolve().parent.parent


def render_template_text(
    template_path: Path,
    replacements: Mapping[str, str],
    fallback: str | None = None,
) -> str:
    if template_path.exists():
        content = template_path.read_text(encoding="utf-8")
        for key, value in replacements.items():
            content = content.replace(key, value)
        return content
    if fallback is not None:
        return fallback
    raise FileNotFoundError(f"Template file not found: {template_path}")


def read_template(template_name: str, root_dir: Path | None = None) -> str:
    template_path = _repo_root(root_dir) / "templates" / template_name
    if not template_path.exists():
        return ""
    return template_path.read_text(encoding="utf-8")


def render_index_document(context, root_dir: Path | None = None) -> str:
    content = read_template("INDEX.md.template", root_dir)
    if not content:
        content = f"""# Module: {context.module_name}

## 职责
[一句话说明模块做什么]

## 关键文件
- `{context.entry_file}`: 入口
- `configs/default.json`: 配置
- `tests/smoke.py`: 冒烟测试

## 调用入口
- `module_name`: `{context.module_name}`
- `entry_file`: `{context.entry_file}`
- `call_path`: `{context.call_path}`
- `call_entry`: `{context.call_entry}`

## 依赖
- 外部依赖: [列出 pip/npm 包]
- 内部依赖: [列出其他模块]

## 快速验证
```bash
python tests/smoke.py
```

## 维护注意事项
[列出关键约束、已知问题、特殊配置等]
"""
    replacements = {
        "{{MODULE_NAME}}": context.module_name,
        "{{ENTRY_FILE}}": context.entry_file,
        "{{CALL_PATH}}": context.call_path,
        "{{CALL_ENTRY}}": context.call_entry,
        "{{DATE}}": datetime.now().strftime("%Y-%m-%d"),
    }
    template_path = _repo_root(root_dir) / "templates" / "INDEX.md.template"
    content = render_template_text(template_path, replacements, content)
    marker_section = render_marker_section(context.marker_rules)
    if "## 关键标记" not in content:
        content = content.rstrip() + "\n\n" + marker_section + "\n"
    if "## 调用入口" not in content:
        content = content.rstrip() + "\n\n" + (
            f"## 调用入口\n- `module_name`: `{context.module_name}`\n- `entry_file`: `{context.entry_file}`\n- `call_path`: `{context.call_path}`\n- `call_entry`: `{context.call_entry}`\n"
        )
    return content.rstrip() + "\n"


def render_spec_document(context, root_dir: Path | None = None) -> str:
    content = read_template("SPEC.md.template", root_dir)
    if not content:
        content = f"""# 接口规范: {context.module_name}

## 调用入口
- `entry_file`: `{context.entry_file}`
- `call_path`: `{context.call_path}`
- `call_entry`: `{context.call_entry}`

## 输入

## 输出

## 配置

## 错误处理

## 示例
"""
    replacements = {
        "{{MODULE_NAME}}": context.module_name,
        "{{ENTRY_FILE}}": context.entry_file,
        "{{CALL_PATH}}": context.call_path,
        "{{CALL_ENTRY}}": context.call_entry,
        "{{DATE}}": datetime.now().strftime("%Y-%m-%d"),
    }
    template_path = _repo_root(root_dir) / "templates" / "SPEC.md.template"
    content = render_template_text(template_path, replacements, content)
    marker_section = render_marker_section(context.marker_rules)
    if "## 调用入口" not in content:
        content = content.rstrip() + "\n\n" + (
            f"## 调用入口\n- `entry_file`: `{context.entry_file}`\n- `call_path`: `{context.call_path}`\n- `call_entry`: `{context.call_entry}`\n"
        )
    if "## 关键标记" not in content:
        content = content.rstrip() + "\n\n" + marker_section + "\n"
    return content.rstrip() + "\n"


def render_changelog_document(context, root_dir: Path | None = None) -> str:
    content = read_template("CHANGELOG.md.template", root_dir)
    if not content:
        content = f"""# Changelog: {context.module_name}

## [Unreleased]

## [1.0.0] - {datetime.now().strftime("%Y-%m-%d")}
### Added
- 初始化模块
- 实现最小协议骨架
"""
    replacements = {
        "{{MODULE_NAME}}": context.module_name,
        "{{DATE}}": datetime.now().strftime("%Y-%m-%d"),
    }
    template_path = _repo_root(root_dir) / "templates" / "CHANGELOG.md.template"
    return render_template_text(template_path, replacements, content).rstrip() + "\n"


def render_init_entry_stub(module_name: str) -> str:
    return f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auto-generated entry stub for {module_name}."""

from __future__ import annotations

from json import dumps


def run() -> dict:
    return {{
        "status": "success",
        "module": "{module_name}",
        "message": "TODO: implement module behavior",
    }}


def main() -> int:
    print(dumps(run(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''


def render_init_smoke_test(module_name: str) -> str:
    return f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auto-generated smoke test for {module_name}."""

from __future__ import annotations

import io
import sys
from pathlib import Path


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from main import run  # noqa: E402


def main() -> int:
    result = run()
    assert result["status"] == "success"
    print("[PASS] smoke test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''


def render_apply_smoke_test(module_name: str) -> str:
    return f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Smoke test placeholder for {module_name}."""

from __future__ import annotations


def main() -> int:
    print("[TODO] implement smoke test")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''


def render_default_config() -> str:
    return json.dumps({"timeout": 30}, ensure_ascii=False, indent=2) + "\n"

