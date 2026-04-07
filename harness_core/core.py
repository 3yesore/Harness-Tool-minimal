"""Core protocol, workflows, and scaffold helpers for Harness Tool."""

from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .markers import (
    DEFAULT_RECOMMENDED_MARKER_KEYS,
    DEFAULT_REQUIRED_MARKER_KEYS,
    MarkerRule,
    build_marker_registry,
)
from .rendering import (
    render_apply_smoke_test,
    render_changelog_document,
    render_default_config,
    render_index_document,
    render_init_entry_stub,
    render_init_smoke_test,
    render_spec_document,
)


DISCOVERY_STAGE = "Discovery"
CONTRACT_STAGE = "Contract"
VALIDATE_STAGE = "Validate"
SUGGEST_STAGE = "Suggest"

CORE_PROTOCOL_VERSION = "v1.0.1 beta"
CORE_STAGE_SEQUENCE = (
    DISCOVERY_STAGE,
    CONTRACT_STAGE,
    VALIDATE_STAGE,
    SUGGEST_STAGE,
)

CORE_EXTENSION_POINTS = (
    "profiles",
    "templates",
    "marker",
    "override",
)

CORE_BOUNDARIES = {
    "version": CORE_PROTOCOL_VERSION,
    "core": "Thin protocol layer for module context, contract, validation, and scaffold plans.",
    "contract": "Frozen contract rules for files, sections, markers, and validation gates.",
    "workflow": "Discovery -> Contract -> Validate -> Suggest.",
    "extension": "Profiles, templates, marker rules, and override points remain explicit.",
    "extension_points": ", ".join(CORE_EXTENSION_POINTS),
}

EXTENSION_GUIDANCE = {
    "profiles": "Tune preset rules and validation severity only. Never redefine the frozen contract.",
    "templates": "Change the default scaffold shape only. Keep required sections and marker keys intact.",
    "marker": "Describe key paths, variables, and coupling explicitly. Do not replace contract checks with comments.",
    "override": "Allow project-local overrides only. Never bypass required files, required sections, or required markers.",
}


def describe_core_boundaries() -> str:
    return "\n".join(f"- {name}: {description}" for name, description in CORE_BOUNDARIES.items())


def describe_development_guidance() -> str:
    return (
        f"Harness Tool {CORE_PROTOCOL_VERSION} keeps a thin core and explicit extension boundaries.\n"
        "Core objects are frozen, workflow stages are explicit, and project-local overrides must stay within contract boundaries.\n"
        f"Workflow stages: {' -> '.join(CORE_STAGE_SEQUENCE)}."
    )


def describe_extension_guidance() -> str:
    return "\n".join(f"- {name}: {description}" for name, description in EXTENSION_GUIDANCE.items())


def _repo_root(root_dir: Path | None = None) -> Path:
    return Path(root_dir) if root_dir is not None else Path(__file__).resolve().parent.parent


def normalize_relpath(value: str | Path) -> str:
    return Path(str(value).replace("\\", "/")).as_posix().lstrip("./")


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_profile_rules(profile_name: str, root_dir: Path | None = None) -> dict[str, Any]:
    root = _repo_root(root_dir)
    profile_path = root / "profiles" / f"{profile_name}.rules.json"
    if not profile_path.exists():
        profile_path = root / "profiles" / "default.rules.json"
    return _read_json(profile_path)


@dataclass(frozen=True)
class ContractRules:
    profile: str
    required_files: tuple[str, ...]
    recommended_files: tuple[str, ...]
    required_index_sections: tuple[str, ...]
    required_spec_sections: tuple[str, ...]
    recommended_paths: tuple[str, ...]
    required_marker_keys: tuple[str, ...] = DEFAULT_REQUIRED_MARKER_KEYS
    recommended_marker_keys: tuple[str, ...] = DEFAULT_RECOMMENDED_MARKER_KEYS
    entry_consistency_mode: str = "soft"
    marker_consistency_mode: str = "soft"


@dataclass(frozen=True)
class ModuleContext:
    module_path: Path
    root_path: Path
    module_name: str
    profile: str
    contract: ContractRules
    structure: dict[str, Any]
    entry_file: str
    call_path: str
    call_entry: str
    marker_rules: tuple[MarkerRule, ...]
    key_files: tuple[str, ...]
    discovered_files: tuple[str, ...]
    discovered_python_files: tuple[str, ...]
    discovered_test_files: tuple[str, ...]
    discovered_config_files: tuple[str, ...]
    risk_summary: tuple[str, ...] = ()


@dataclass
class ValidationResult:
    status: str = "success"
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    next_actions: list[str] = field(default_factory=list)
    patch_draft: list[str] = field(default_factory=list)
    stage_trace: list[str] = field(default_factory=list)
    context: ModuleContext | None = None

    def add_stage(self, stage: str) -> None:
        if stage not in self.stage_trace:
            self.stage_trace.append(stage)

    def add_error(self, message: str) -> None:
        self.errors.append(message)

    def add_warning(self, message: str) -> None:
        self.warnings.append(message)

    def add_note(self, message: str) -> None:
        self.notes.append(message)

    def add_next_action(self, message: str) -> None:
        self.next_actions.append(message)

    def add_patch_line(self, message: str) -> None:
        self.patch_draft.append(message)

    def exit_code(self, strict: bool = False) -> int:
        if self.errors:
            return 1
        if strict and self.warnings:
            return 1
        return 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "errors": list(self.errors),
            "warnings": list(self.warnings),
            "notes": list(self.notes),
            "next_actions": list(self.next_actions),
            "patch_draft": list(self.patch_draft),
            "stage_trace": list(self.stage_trace),
            "context": None
            if self.context is None
            else {
                "module_name": self.context.module_name,
                "module_path": str(self.context.module_path),
                "profile": self.context.profile,
                "entry_file": self.context.entry_file,
                "call_path": self.context.call_path,
                "call_entry": self.context.call_entry,
            },
        }

    def render_text(self) -> str:
        lines = [
            "=" * 72,
            f"Status: {self.status}",
        ]
        if self.stage_trace:
            lines.append(f"Stages: {' -> '.join(self.stage_trace)}")
        if self.context is not None:
            lines.extend(
                [
                    f"Module: {self.context.module_name}",
                    f"Path: {self.context.module_path}",
                    f"Profile: {self.context.profile}",
                ]
            )
        if self.notes:
            lines.append("")
            lines.append("Notes:")
            lines.extend(f"  - {item}" for item in self.notes)
        if self.warnings:
            lines.append("")
            lines.append("Warnings:")
            lines.extend(f"  - {item}" for item in self.warnings)
        if self.errors:
            lines.append("")
            lines.append("Errors:")
            lines.extend(f"  - {item}" for item in self.errors)
        if self.next_actions:
            lines.append("")
            lines.append("Next actions:")
            lines.extend(f"  - {item}" for item in self.next_actions)
        if self.patch_draft:
            lines.append("")
            lines.append("Patch draft:")
            lines.extend(f"  - {item}" for item in self.patch_draft)
        lines.append("=" * 72)
        return "\n".join(lines)


@dataclass(frozen=True)
class ScaffoldPlan:
    operation: str
    module_name: str
    module_path: Path
    profile: str
    create_dirs: tuple[str, ...] = ()
    create_files: dict[str, str] = field(default_factory=dict)
    existing_files: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()
    entry_file: str = "src/main.py"
    call_path: str = "src/main.py"
    call_entry: str = "src/main.py"


def _unique_paths(paths: list[str]) -> tuple[str, ...]:
    seen: set[str] = set()
    items: list[str] = []
    for path in paths:
        normalized = normalize_relpath(path)
        if normalized and normalized not in seen:
            seen.add(normalized)
            items.append(normalized)
    return tuple(items)


def _choose_entry_file(all_files: list[str], python_files: list[str]) -> str:
    for candidate in ("src/main.py", "main.py"):
        if candidate in all_files:
            return candidate

    src_candidates = sorted(
        path for path in python_files if path.startswith("src/") and "main" in Path(path).stem.lower()
    )
    if src_candidates:
        return src_candidates[0]

    non_test_python = [path for path in python_files if "test" not in path.lower() and not path.startswith("harness/")]
    if non_test_python:
        return sorted(non_test_python)[0]

    if python_files:
        return sorted(python_files)[0]

    return "src/main.py"


def _choose_call_path(all_files: list[str], entry_file: str) -> str:
    for candidate in (
        "harness/run_harness.py",
        "run_harness.py",
        "tools/run_harness.py",
        "scripts/run_harness.py",
        "src/main.py",
        "main.py",
        entry_file,
    ):
        if candidate in all_files:
            return candidate
    return entry_file


def _discover_structure(module_path: Path) -> dict[str, Any]:
    files = [path.relative_to(module_path).as_posix() for path in module_path.rglob("*") if path.is_file()]
    python_files = [path for path in files if path.endswith(".py")]
    config_files = [path for path in files if path.endswith((".json", ".yaml", ".yml"))]
    test_files = [path for path in python_files if "test" in Path(path).name.lower() or "test" in path.lower()]
    docs_files = [path for path in files if path.startswith("docs/") or Path(path).suffix.lower() in {".md", ".rst"}]

    entry_file = _choose_entry_file(files, python_files)
    call_path = _choose_call_path(files, entry_file)
    call_entry = entry_file
    marker_source = None
    if (module_path / "harness" / "extensions" / "marker_rules.py").exists():
        marker_source = normalize_relpath("harness/extensions/marker_rules.py")

    return {
        "files": tuple(files),
        "python_files": tuple(python_files),
        "config_files": tuple(config_files),
        "test_files": tuple(test_files),
        "docs_files": tuple(docs_files),
        "has_src": (module_path / "src").exists(),
        "has_tests": (module_path / "tests").exists(),
        "has_configs": (module_path / "configs").exists(),
        "has_docs": (module_path / "docs").exists(),
        "entry_file": entry_file,
        "call_path": call_path,
        "call_entry": call_entry,
        "marker_source": marker_source,
    }


def build_contract_rules(profile_name: str, root_dir: Path | None = None) -> ContractRules:
    rules = load_profile_rules(profile_name, root_dir=root_dir)
    return ContractRules(
        profile=rules.get("profile", profile_name),
        required_files=tuple(rules.get("required_files", ["INDEX.md", "SPEC.md"])),
        recommended_files=tuple(rules.get("recommended_files", ["CHANGELOG.md"])),
        required_index_sections=tuple(
            rules.get(
                "required_index_sections",
                [
                    "## 职责",
                    "## 关键文件",
                    "## 调用入口",
                    "## 关键标记",
                    "## 依赖",
                    "## 快速验证",
                    "## 维护注意事项",
                ],
            )
        ),
        required_spec_sections=tuple(
            rules.get(
                "required_spec_sections",
                [
                    "## 输入",
                    "## 调用入口",
                    "## 输出",
                    "## 配置",
                    "## 错误处理",
                    "## 示例",
                    "## 关键标记",
                ],
            )
        ),
        recommended_paths=tuple(rules.get("recommended_paths", [])),
        required_marker_keys=tuple(rules.get("required_marker_keys", list(DEFAULT_REQUIRED_MARKER_KEYS))),
        recommended_marker_keys=tuple(rules.get("recommended_marker_keys", list(DEFAULT_RECOMMENDED_MARKER_KEYS))),
        entry_consistency_mode=rules.get("entry_consistency_mode", "soft"),
        marker_consistency_mode=rules.get("marker_consistency_mode", "soft"),
    )


def _summarize_risks(structure: dict[str, Any], contract: ContractRules) -> tuple[str, ...]:
    risks: list[str] = []
    if not structure["test_files"]:
        risks.append("No Python tests discovered.")
    if not structure["config_files"]:
        risks.append("No config files discovered.")
    if "INDEX.md" not in structure["files"]:
        risks.append("INDEX.md is missing.")
    if "SPEC.md" not in structure["files"]:
        risks.append("SPEC.md is missing.")
    if contract.marker_consistency_mode == "soft":
        risks.append("Marker consistency runs in soft mode by default.")
    return tuple(risks)


def build_module_context(
    module_path: str | Path,
    profile: str = "default",
    root_dir: Path | None = None,
) -> ModuleContext:
    root = _repo_root(root_dir)
    module = Path(module_path)
    if not module.exists():
        raise FileNotFoundError(f"Module path does not exist: {module}")
    if not module.is_dir():
        raise NotADirectoryError(f"Module path is not a directory: {module}")

    structure = _discover_structure(module)
    contract = build_contract_rules(profile, root_dir=root)
    marker_rules = build_marker_registry(
        entry_file=structure["entry_file"],
        call_path=structure["call_path"],
        call_entry=structure["call_entry"],
        smoke_test="tests/smoke.py",
        config_file=structure["config_files"][0] if structure["config_files"] else "configs/default.json",
        marker_source=structure["marker_source"],
    )
    key_files = _unique_paths(
        [
            "INDEX.md",
            "SPEC.md",
            "CHANGELOG.md",
            structure["entry_file"],
            structure["call_path"],
            structure["call_entry"],
            "tests/smoke.py",
            "configs/default.json",
            *structure["config_files"],
            *structure["test_files"],
        ]
    )

    return ModuleContext(
        module_path=module.resolve(),
        root_path=root,
        module_name=module.name,
        profile=contract.profile,
        contract=contract,
        structure=structure,
        entry_file=structure["entry_file"],
        call_path=structure["call_path"],
        call_entry=structure["call_entry"],
        marker_rules=marker_rules,
        key_files=key_files,
        discovered_files=structure["files"],
        discovered_python_files=structure["python_files"],
        discovered_test_files=structure["test_files"],
        discovered_config_files=structure["config_files"],
        risk_summary=_summarize_risks(structure, contract),
    )


def _plan_context(module_path: Path, module_name: str, profile: str, root: Path) -> ModuleContext:
    contract = build_contract_rules(profile, root_dir=root)
    structure = {
        "files": tuple(),
        "python_files": tuple(),
        "config_files": tuple(),
        "test_files": tuple(),
        "docs_files": tuple(),
        "has_src": True,
        "has_tests": True,
        "has_configs": True,
        "has_docs": True,
        "entry_file": "src/main.py",
        "call_path": "src/main.py",
        "call_entry": "src/main.py",
        "marker_source": None,
    }
    marker_rules = build_marker_registry(
        entry_file="src/main.py",
        call_path="src/main.py",
        call_entry="src/main.py",
        smoke_test="tests/smoke.py",
        config_file="configs/default.json",
    )
    return ModuleContext(
        module_path=module_path,
        root_path=root,
        module_name=module_name,
        profile=contract.profile,
        contract=contract,
        structure=structure,
        entry_file="src/main.py",
        call_path="src/main.py",
        call_entry="src/main.py",
        marker_rules=marker_rules,
        key_files=("INDEX.md", "SPEC.md", "CHANGELOG.md", "src/main.py", "tests/smoke.py", "configs/default.json"),
        discovered_files=tuple(),
        discovered_python_files=tuple(),
        discovered_test_files=tuple(),
        discovered_config_files=tuple(),
        risk_summary=tuple(),
    )


def _resolve_base_dir(path: str | Path, root: Path) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else root / candidate


def build_init_plan(
    module_name: str,
    output_dir: str = "modules",
    profile: str = "default",
    root_dir: Path | None = None,
) -> ScaffoldPlan:
    root = _repo_root(root_dir)
    module_path = _resolve_base_dir(output_dir, root) / module_name
    context = _plan_context(module_path.resolve(), module_name, profile, root)
    return ScaffoldPlan(
        operation="init",
        module_name=context.module_name,
        module_path=context.module_path,
        profile=context.profile,
        create_dirs=("src", "tests", "configs", "docs"),
        create_files={
            "INDEX.md": render_index_document(context, root_dir=context.root_path),
            "SPEC.md": render_spec_document(context, root_dir=context.root_path),
            "CHANGELOG.md": render_changelog_document(context, root_dir=context.root_path),
            "src/main.py": render_init_entry_stub(context.module_name),
            "tests/smoke.py": render_init_smoke_test(context.module_name),
            "configs/default.json": render_default_config(),
        },
        existing_files=tuple(),
        notes=("Generated skeleton is intentionally thin and protocol-driven.",),
        entry_file=context.entry_file,
        call_path=context.call_path,
        call_entry=context.call_entry,
    )


def build_apply_plan(
    module_path: str | Path,
    profile: str = "default",
    root_dir: Path | None = None,
) -> ScaffoldPlan:
    root = _repo_root(root_dir)
    module = _resolve_base_dir(module_path, root)
    if not module.exists():
        raise FileNotFoundError(f"Module path does not exist: {module}")

    context = build_module_context(module, profile=profile, root_dir=root)
    create_dirs = [name for name in ("src", "tests", "configs", "docs") if not (module / name).exists()]
    create_files: dict[str, str] = {}

    if not (module / "INDEX.md").exists():
        create_files["INDEX.md"] = render_index_document(context, root_dir=root)
    if not (module / "SPEC.md").exists():
        create_files["SPEC.md"] = render_spec_document(context, root_dir=root)
    if not (module / "CHANGELOG.md").exists():
        create_files["CHANGELOG.md"] = render_changelog_document(context, root_dir=root)
    if not (module / "src" / "main.py").exists():
        create_files["src/main.py"] = render_init_entry_stub(context.module_name)
    if not (module / "tests" / "smoke.py").exists():
        create_files["tests/smoke.py"] = render_apply_smoke_test(context.module_name)
    if not (module / "configs" / "default.json").exists():
        create_files["configs/default.json"] = render_default_config()

    notes = ["Project-local extension folders remain project-owned and optional."]
    if context.risk_summary:
        notes.extend(context.risk_summary)

    return ScaffoldPlan(
        operation="apply",
        module_name=context.module_name,
        module_path=context.module_path,
        profile=context.profile,
        create_dirs=tuple(create_dirs),
        create_files=create_files,
        existing_files=tuple(sorted(set(context.discovered_files).intersection(create_files.keys()))),
        notes=tuple(notes),
        entry_file=context.entry_file,
        call_path=context.call_path,
        call_entry=context.call_entry,
    )


def _materialize(plan: ScaffoldPlan) -> list[str]:
    created: list[str] = []
    for relpath in plan.create_dirs:
        (plan.module_path / relpath).mkdir(parents=True, exist_ok=True)
    for relpath, content in plan.create_files.items():
        target = plan.module_path / relpath
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            target.write_text(content, encoding="utf-8")
            created.append(relpath)
    return created


def init_module(
    module_name: str,
    output_dir: str = "modules",
    profile: str = "default",
    root_dir: Path | None = None,
) -> ScaffoldPlan:
    plan = build_init_plan(module_name, output_dir=output_dir, profile=profile, root_dir=root_dir)
    _materialize(plan)
    return plan


def apply_harness(
    module_path: str | Path,
    profile: str = "default",
    root_dir: Path | None = None,
) -> ScaffoldPlan:
    plan = build_apply_plan(module_path, profile=profile, root_dir=root_dir)
    _materialize(plan)
    return plan


def _normalize_heading(value: str) -> str:
    return value.strip().lstrip("#").strip()


def _has_heading(content: str, title: str) -> bool:
    pattern = rf"^##\s+{re.escape(_normalize_heading(title))}\s*$"
    return re.search(pattern, content, flags=re.MULTILINE) is not None


def _extract_section(content: str, title: str) -> str:
    pattern = rf"^##\s+{re.escape(_normalize_heading(title))}\s*$\n(.*?)(?=^##\s|\Z)"
    match = re.search(pattern, content, flags=re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else ""


def _collect_section_map(section: str) -> dict[str, str]:
    items: dict[str, str] = {}
    for line in section.splitlines():
        match = re.match(r"^\s*-\s*`?(?P<key>[^`:]+?)`?\s*[:：]\s*`?(?P<value>.+?)`?\s*$", line.strip())
        if not match:
            continue
        key = match.group("key").strip()
        value = re.sub(r"\s*\(.*\)\s*$", "", match.group("value").strip()).strip("`").strip()
        items[key] = value
    return items


def _collect_section_backticks(section: str) -> tuple[str, ...]:
    return tuple(normalize_relpath(item) for item in re.findall(r"`([^`]+)`", section))


def _path_exists(module_path: Path, relpath: str) -> bool:
    return (module_path / normalize_relpath(relpath)).exists()


def _validate_required_files(context: ModuleContext, result: ValidationResult) -> None:
    for relpath in context.contract.required_files:
        if not _path_exists(context.module_path, relpath):
            result.add_error(f"Missing required file: {relpath}")
        else:
            result.add_note(f"[OK] required file: {relpath}")


def _validate_changelog(context: ModuleContext, result: ValidationResult) -> None:
    changelog = context.module_path / "CHANGELOG.md"
    if not changelog.exists():
        result.add_warning("CHANGELOG.md is missing; recommended for tracking protocol changes.")
        return
    content = changelog.read_text(encoding="utf-8")
    if not re.search(r"\[[\d\.]+\]", content):
        result.add_warning("CHANGELOG.md should contain version brackets like [1.0.0].")
    if not re.search(r"\d{4}-\d{2}-\d{2}", content):
        result.add_warning("CHANGELOG.md should contain a YYYY-MM-DD date.")


def _validate_sections(
    context: ModuleContext,
    result: ValidationResult,
    filename: str,
    required_sections: tuple[str, ...],
) -> str:
    path = context.module_path / filename
    content = path.read_text(encoding="utf-8")
    for section in required_sections:
        if _has_heading(content, section):
            result.add_note(f"[OK] {filename} contains {section}")
        else:
            result.add_error(f"{filename} is missing required section: {section}")
    return content


def _validate_paths_in_map(
    context: ModuleContext,
    result: ValidationResult,
    section_map: dict[str, str],
    required_keys: tuple[str, ...],
    optional_keys: tuple[str, ...] = (),
    section_name: str = "section",
) -> None:
    for key in required_keys:
        value = section_map.get(key)
        if not value:
            result.add_error(f"{section_name} is missing required marker: {key}")
            continue
        if not _path_exists(context.module_path, value):
            result.add_error(f"{section_name} marker points to missing path: {key} -> {value}")
    for key in optional_keys:
        value = section_map.get(key)
        if value and not _path_exists(context.module_path, value):
            result.add_warning(f"{section_name} marker points to missing recommended path: {key} -> {value}")


def _validate_entry_consistency(
    context: ModuleContext,
    result: ValidationResult,
    index_call: dict[str, str],
    spec_call: dict[str, str],
) -> None:
    index_entry = normalize_relpath(index_call.get("entry_file", ""))
    spec_entry = normalize_relpath(spec_call.get("call_entry", ""))
    if not index_entry or not spec_entry:
        result.add_error("entry_file and call_entry must be declared in INDEX.md and SPEC.md.")
        return
    if index_entry != spec_entry:
        message = f"entry mismatch: INDEX.md entry_file={index_entry}, SPEC.md call_entry={spec_entry}"
        if context.contract.entry_consistency_mode == "strict":
            result.add_error(message)
        else:
            result.add_warning(message)

    if index_call.get("call_path") and spec_call.get("call_path"):
        index_call_path = normalize_relpath(index_call["call_path"])
        spec_call_path = normalize_relpath(spec_call["call_path"])
        if index_call_path != spec_call_path:
            message = f"call path mismatch: INDEX.md call_path={index_call_path}, SPEC.md call_path={spec_call_path}"
            if context.contract.entry_consistency_mode == "strict":
                result.add_error(message)
            else:
                result.add_warning(message)


def _validate_marker_consistency(
    context: ModuleContext,
    result: ValidationResult,
    index_markers: dict[str, str],
    spec_markers: dict[str, str],
) -> None:
    expected: dict[str, str] = {
        "entry_file": context.entry_file,
        "call_path": context.call_path,
        "call_entry": context.call_entry,
    }
    for key in context.contract.required_marker_keys:
        index_value = normalize_relpath(index_markers.get(key, ""))
        spec_value = normalize_relpath(spec_markers.get(key, ""))
        expected_value = normalize_relpath(expected.get(key, index_value or spec_value))
        if not index_value:
            result.add_error(f"INDEX.md marker section is missing required key: {key}")
        if not spec_value:
            result.add_error(f"SPEC.md marker section is missing required key: {key}")
        if expected_value:
            if index_value and index_value != expected_value:
                result.add_warning(f"INDEX.md marker mismatch for {key}: {index_value} != {expected_value}")
            if spec_value and spec_value != expected_value:
                result.add_warning(f"SPEC.md marker mismatch for {key}: {spec_value} != {expected_value}")

    for key in context.contract.recommended_marker_keys:
        value = normalize_relpath(index_markers.get(key, "") or spec_markers.get(key, ""))
        if value and not _path_exists(context.module_path, value):
            message = f"marker path missing: {key} -> {value}"
            if context.contract.marker_consistency_mode == "strict":
                result.add_error(message)
            else:
                result.add_warning(message)


def _safe_module_id(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]+", "_", value).strip("_") or "module"


def _adapter_shell_paths(module_path: Path) -> dict[str, Any] | None:
    adapter_root = module_path / "adapters"
    protocol_doc = module_path / "ADAPTER_PROTOCOL.md"
    if not adapter_root.exists() and not protocol_doc.exists():
        return None

    sample_files = tuple(
        normalize_relpath(path.relative_to(module_path).as_posix())
        for path in sorted(adapter_root.glob("*.py"))
        if path.name not in {"__init__.py", "protocol.py"}
    ) if adapter_root.exists() else tuple()

    return {
        "adapter_root": adapter_root,
        "protocol_doc": protocol_doc,
        "readme": adapter_root / "README.md",
        "protocol_py": adapter_root / "protocol.py",
        "sample_files": sample_files,
    }


def _import_module_from_file(path: Path, module_name: str) -> Any:
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot create import spec for {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _validate_adapter_protocol_module(module: Any, result: ValidationResult) -> None:
    required_symbols = (
        "ADAPTER_PROTOCOL_VERSION",
        "ADAPTER_LIFECYCLE",
        "AdapterSpec",
        "AdapterContext",
        "AdapterResult",
        "describe_adapter_protocol",
    )
    for symbol in required_symbols:
        if not hasattr(module, symbol):
            result.add_error(f"Adapter protocol shell is missing required symbol: {symbol}")
        else:
            result.add_note(f"[OK] adapter protocol exports {symbol}")

    lifecycle = getattr(module, "ADAPTER_LIFECYCLE", ())
    if not isinstance(lifecycle, (tuple, list)) or not lifecycle:
        result.add_error("ADAPTER_LIFECYCLE must be a non-empty tuple or list.")

    version = getattr(module, "ADAPTER_PROTOCOL_VERSION", "")
    if not isinstance(version, str) or not version.strip():
        result.add_error("ADAPTER_PROTOCOL_VERSION must be a non-empty string.")

    describe = getattr(module, "describe_adapter_protocol", None)
    if callable(describe):
        try:
            rendered = str(describe())
        except Exception as exc:  # pragma: no cover - defensive shell validation
            result.add_error(f"describe_adapter_protocol() failed to render: {exc}")
        else:
            if "Adapter protocol version" not in rendered:
                result.add_warning("Adapter protocol description should include a visible version line.")
    else:
        result.add_error("describe_adapter_protocol must be callable.")


def _validate_adapter_sample_module(module: Any, result: ValidationResult, sample_path: Path) -> None:
    public_names = [name for name in dir(module) if not name.startswith("_")]
    if not any(name.endswith("Adapter") for name in public_names) and not any(name.startswith("build_") for name in public_names):
        result.add_warning(
            f"{sample_path.relative_to(sample_path.parent.parent)} does not expose a public adapter class or factory."
        )


def _validate_adapter_shell(context: ModuleContext, result: ValidationResult) -> None:
    shell = _adapter_shell_paths(context.module_path)
    if shell is None:
        return

    result.add_note("[OK] adapter envelope detected")

    protocol_doc = shell["protocol_doc"]
    adapter_root = shell["adapter_root"]
    readme = shell["readme"]
    protocol_py = shell["protocol_py"]
    sample_files = shell["sample_files"]

    if not protocol_doc.exists():
        result.add_error("Adapter envelope is missing ADAPTER_PROTOCOL.md.")
    else:
        result.add_note("[OK] adapter protocol doc exists: ADAPTER_PROTOCOL.md")

    if not adapter_root.exists():
        result.add_error("Adapter envelope is missing adapters/ directory.")
        return

    if not readme.exists():
        result.add_error("Adapter envelope is missing adapters/README.md.")
    else:
        readme_text = readme.read_text(encoding="utf-8")
        lowered = readme_text.lower()
        if "protocol" not in lowered or ("not a second core" not in lowered and "protocol-first" not in lowered):
            result.add_warning("adapters/README.md should describe the folder as a protocol shell, not a second core.")
        else:
            result.add_note("[OK] adapters/README.md describes a protocol shell")

    if not protocol_py.exists():
        result.add_error("Adapter envelope is missing adapters/protocol.py.")
    else:
        module_name = f"_harness_adapter_protocol_{_safe_module_id(context.module_name)}"
        try:
            protocol_module = _import_module_from_file(protocol_py, module_name)
        except Exception as exc:  # pragma: no cover - defensive shell validation
            result.add_error(f"Failed to import adapters/protocol.py: {exc}")
        else:
            _validate_adapter_protocol_module(protocol_module, result)

    if not sample_files:
        result.add_warning("Adapter envelope was detected, but no sample adapter modules were found.")
        return

    for relpath in sample_files:
        sample_path = context.module_path / relpath
        module_name = f"_harness_adapter_sample_{_safe_module_id(context.module_name)}_{sample_path.stem}"
        try:
            sample_module = _import_module_from_file(sample_path, module_name)
        except Exception as exc:  # pragma: no cover - defensive shell validation
            result.add_error(f"Failed to import adapter sample {relpath}: {exc}")
            continue
        result.add_note(f"[OK] adapter sample importable: {relpath}")
        _validate_adapter_sample_module(sample_module, result, sample_path)


def _validate_key_file_lists(
    context: ModuleContext,
    result: ValidationResult,
    index_content: str,
    index_call: dict[str, str],
) -> None:
    key_section = _extract_section(index_content, "关键文件")
    key_files = _collect_section_backticks(key_section)
    for marker_name in ("entry_file", "call_entry"):
        expected_path = normalize_relpath(index_call.get(marker_name, ""))
        if expected_path and expected_path not in key_files:
            message = f"INDEX.md key files should include {marker_name}: {expected_path}"
            if context.contract.entry_consistency_mode == "strict":
                result.add_error(message)
            else:
                result.add_warning(message)


def _validate_quick_verification(
    context: ModuleContext,
    result: ValidationResult,
    index_content: str,
) -> None:
    quick_section = _extract_section(index_content, "快速验证")
    if not quick_section:
        result.add_warning("INDEX.md should contain a quick verification command.")
        return
    commands = re.findall(r"```(?:bash|sh|python)?\s*\n(.*?)\n```", quick_section, flags=re.DOTALL)
    if not commands:
        result.add_warning("INDEX.md quick verification section should contain a code block.")
        return
    for command_block in commands:
        if "tests/smoke.py" in command_block and not _path_exists(context.module_path, "tests/smoke.py"):
            result.add_error("Quick verification references tests/smoke.py, but it does not exist.")


def _validate_tests(context: ModuleContext, result: ValidationResult) -> None:
    tests_dir = context.module_path / "tests"
    if not tests_dir.exists():
        result.add_error("Missing tests/ directory.")
        return
    smoke = tests_dir / "smoke.py"
    if not smoke.exists():
        result.add_error("Missing tests/smoke.py smoke test.")
    py_tests = list(tests_dir.glob("*.py"))
    if not py_tests:
        result.add_warning("tests/ directory exists but contains no Python tests.")


def _run_smoke_test(context: ModuleContext, result: ValidationResult) -> None:
    smoke_test = context.module_path / "tests" / "smoke.py"
    if not smoke_test.exists():
        return
    try:
        completed = subprocess.run(
            [sys.executable, "tests/smoke.py"],
            cwd=context.module_path,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except Exception as exc:
        result.add_error(f"Smoke test execution failed: {exc}")
        return
    stdout_text = completed.stdout or ""
    stderr_text = completed.stderr or ""
    if stdout_text.strip():
        result.add_note(stdout_text.rstrip())
    if stderr_text.strip():
        result.add_warning(stderr_text.rstrip())
    if completed.returncode != 0:
        result.add_error(f"Smoke test returned non-zero exit code: {completed.returncode}")


def _validate_configs(context: ModuleContext, result: ValidationResult) -> None:
    configs_dir = context.module_path / "configs"
    if not configs_dir.exists():
        result.add_warning("configs/ directory is missing.")
        return
    for config_file in configs_dir.glob("*.json"):
        try:
            json.loads(config_file.read_text(encoding="utf-8"))
        except Exception as exc:
            result.add_error(f"Invalid JSON config: {config_file.relative_to(context.module_path)} ({exc})")


def _validate_recommended_paths(context: ModuleContext, result: ValidationResult) -> None:
    for path_name in context.contract.recommended_paths:
        if not (context.module_path / path_name).exists():
            result.add_warning(f"Recommended path missing: {path_name}")

    for file_name in context.contract.recommended_files:
        if not (context.module_path / file_name).exists():
            result.add_warning(f"Recommended file missing: {file_name}")


def _suggest_next_steps(context: ModuleContext, result: ValidationResult) -> None:
    if result.errors:
        result.add_next_action("Fix required files, sections, or marker paths first.")
    if result.warnings and not result.errors:
        result.add_next_action("Review warnings and decide whether to tighten the profile.")
    if not result.errors and not result.warnings:
        result.add_next_action("Module is contract-complete. Proceed with normal development.")
    if context.risk_summary:
        for risk in context.risk_summary:
            result.add_note(risk)
    result.add_patch_line("Keep local overrides project-owned and contract-safe.")
    result.add_patch_line("Do not move protocol boundaries into core.")


def validate_module(
    module_path: str | Path,
    profile: str = "default",
    strict: bool = False,
    root_dir: Path | None = None,
) -> ValidationResult:
    context = build_module_context(module_path, profile=profile, root_dir=root_dir)
    result = ValidationResult(context=context)

    result.add_stage(DISCOVERY_STAGE)
    result.add_stage(CONTRACT_STAGE)
    _validate_required_files(context, result)
    _validate_changelog(context, result)

    index_content = ""
    spec_content = ""
    if (context.module_path / "INDEX.md").exists():
        index_content = _validate_sections(context, result, "INDEX.md", context.contract.required_index_sections)
    if (context.module_path / "SPEC.md").exists():
        spec_content = _validate_sections(context, result, "SPEC.md", context.contract.required_spec_sections)

    index_call = _collect_section_map(_extract_section(index_content, "调用入口")) if index_content else {}
    spec_call = _collect_section_map(_extract_section(spec_content, "调用入口")) if spec_content else {}
    index_markers = _collect_section_map(_extract_section(index_content, "关键标记")) if index_content else {}
    spec_markers = _collect_section_map(_extract_section(spec_content, "关键标记")) if spec_content else {}

    if index_content:
        _validate_key_file_lists(context, result, index_content, index_call)
        _validate_quick_verification(context, result, index_content)
    if index_call and spec_call:
        _validate_entry_consistency(context, result, index_call, spec_call)
    if index_markers or spec_markers:
        _validate_marker_consistency(context, result, index_markers, spec_markers)

    _validate_adapter_shell(context, result)

    result.add_stage(VALIDATE_STAGE)
    _validate_tests(context, result)
    _run_smoke_test(context, result)
    _validate_configs(context, result)
    _validate_recommended_paths(context, result)

    result.add_stage(SUGGEST_STAGE)
    _suggest_next_steps(context, result)

    if result.errors:
        result.status = "failure"
    elif result.warnings:
        result.status = "warning"
    else:
        result.status = "success"

    if strict and result.warnings and not result.errors:
        result.add_note("Strict mode treats warnings as fatal for exit code purposes.")

    return result
