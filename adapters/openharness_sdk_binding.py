"""OpenHarness SDK binding shell.

This module keeps the binding narrow:
- consume the exported OpenHarness bridge surface from Harness Tool
- package it into an SDK-facing registration contract
- render a copyable TypeScript sample without hosting the OpenHarness runtime
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

from .openharness_bridge import export_openharness_integration


@dataclass(frozen=True)
class OpenHarnessSdkBinding:
    """Narrow SDK binding shell for OpenHarness."""

    workspace_path: Path

    @property
    def transport_script(self) -> str:
        return "scripts/openharness_validate_transport.py"

    def build_registration_contract(
        self,
        module_path: str | Path,
        *,
        profile: str = "default",
        strict: bool = False,
        include_validation: bool = True,
    ) -> dict[str, Any]:
        """Build the narrow contract that an OpenHarness SDK layer can consume."""
        integration = export_openharness_integration(
            self.workspace_path,
            module_path,
            profile=profile,
            strict=strict,
            include_validation=include_validation,
        )
        return {
            "binding": {
                "target_runtime": "openharness",
                "binding_type": "sdk-shell",
                "host_runtime": False,
                "workspace_path": str(self.workspace_path),
            },
            "integration": integration,
            "transport": {
                "kind": "process",
                "python_command": "python",
                "script_path": self.transport_script,
            },
            "registration": {
                "tool_name": integration["registration"]["tool_definition"]["name"],
                "tool_definition": integration["registration"]["tool_definition"],
                "context_payload": integration["registration"]["context_payload"],
                "provider_hints": integration["registration"]["provider_hints"],
                "middleware_hints": integration["registration"]["middleware_hints"],
                "agent_context_injection": integration["registration"]["agent_context_injection"],
                "skill_snippet": integration["registration"]["skill_snippet"],
                "tool_call_example": integration["examples"]["validate_tool_call"],
            },
        }

    def render_typescript_sample(
        self,
        module_path: str | Path,
        *,
        profile: str = "default",
        strict: bool = False,
        include_validation: bool = True,
    ) -> str:
        """Render a copyable TypeScript binding sample for OpenHarness."""
        contract = self.build_registration_contract(
            module_path,
            profile=profile,
            strict=strict,
            include_validation=include_validation,
        )
        context_payload = json.dumps(contract["registration"]["context_payload"], indent=2)
        provider_hints = json.dumps(contract["registration"]["provider_hints"], indent=2)
        middleware_hints = json.dumps(contract["registration"]["middleware_hints"], indent=2)
        agent_context = json.dumps(contract["registration"]["agent_context_injection"], indent=2)
        skill_snippet = json.dumps(contract["registration"]["skill_snippet"], indent=2)
        tool_call_example = json.dumps(contract["registration"]["tool_call_example"], indent=2)
        workspace_path = json.dumps(contract["binding"]["workspace_path"])
        transport_script = json.dumps(contract["transport"]["script_path"])
        return "\n".join(
            [
                "// OpenHarness SDK binding sample",
                "// This sample uses the real OpenHarness Agent API and a narrow Python process transport.",
                "",
                "import { execFile } from \"node:child_process\";",
                "import { promisify } from \"node:util\";",
                "import { tool, type LanguageModel } from \"ai\";",
                "import { z } from \"zod\";",
                "import { Agent } from \"@openharness/core\";",
                "",
                "const execFileAsync = promisify(execFile);",
                f"const contextPayload = {context_payload} as const;",
                f"const providerHints = {provider_hints} as const;",
                f"const middlewareHints = {middleware_hints} as const;",
                f"const agentContextInjection = {agent_context};",
                f"const skillSnippet = {skill_snippet};",
                f"const toolCallExample = {tool_call_example} as const;",
                f"const workspacePath = {workspace_path};",
                f"const transportScript = {transport_script};",
                "",
                "type HarnessValidateArgs = {",
                "  module_path: string;",
                "  profile?: string;",
                "  strict?: boolean;",
                "};",
                "",
                "async function harnessValidate(args: HarnessValidateArgs) {",
                "  const python = process.env.PYTHON ?? \"python\";",
                "  const cliArgs = [",
                "    transportScript,",
                "    \"--workspace-path\",",
                "    workspacePath,",
                "    \"--module-path\",",
                "    args.module_path,",
                "    \"--profile\",",
                "    args.profile ?? \"default\",",
                "  ];",
                "  if (args.strict) cliArgs.push(\"--strict\");",
                "  const { stdout } = await execFileAsync(python, cliArgs, { cwd: workspacePath });",
                "  return JSON.parse(stdout);",
                "}",
                "",
                "export function buildHarnessAwareAgent(model: LanguageModel) {",
                "  const harnessValidateTool = tool({",
                "    description: \"Run Harness Tool validation as a preflight contract gate.\",",
                "    inputSchema: z.object({",
                "      module_path: z.string(),",
                "      profile: z.string().default(\"default\"),",
                "      strict: z.boolean().default(false),",
                "    }),",
                "    execute: async (args: HarnessValidateArgs) => harnessValidate(args),",
                "  });",
                "",
                "  const agent = new Agent({",
                "    name: \"harness-aware-agent\",",
                "    model,",
                "    systemPrompt: [agentContextInjection, \"\", skillSnippet].join(\"\\n\"),",
                "    tools: {",
                "      harness_validate: harnessValidateTool,",
                "    },",
                "    maxSteps: 20,",
                "  });",
                "",
                "  return { agent, contextPayload, providerHints, middlewareHints, toolCallExample };",
                "}",
            ]
        )

    def export_sdk_binding(
        self,
        module_path: str | Path,
        *,
        profile: str = "default",
        strict: bool = False,
        include_validation: bool = True,
    ) -> dict[str, Any]:
        """Export the full SDK-facing binding surface."""
        contract = self.build_registration_contract(
            module_path,
            profile=profile,
            strict=strict,
            include_validation=include_validation,
        )
        return {
            "binding": contract["binding"],
            "transport": contract["transport"],
            "registration": contract["registration"],
            "typescript_sample": self.render_typescript_sample(
                module_path,
                profile=profile,
                strict=strict,
                include_validation=include_validation,
            ),
            "references": {
                "bridge_spec": "OPENHARNESS_BRIDGE.md",
                "binding_spec": "OPENHARNESS_SDK_BINDING.md",
                "open_items": "docs/OPENHARNESS_SDK_BINDING_OPEN_ITEMS.md",
                "work_index": "docs/OPENHARNESS_SDK_BINDING_INDEX.md",
            },
        }


def build_openharness_sdk_binding(workspace_path: str | Path) -> OpenHarnessSdkBinding:
    return OpenHarnessSdkBinding(workspace_path=Path(workspace_path))


def export_openharness_sdk_binding(
    workspace_path: str | Path,
    module_path: str | Path,
    *,
    profile: str = "default",
    strict: bool = False,
    include_validation: bool = True,
) -> dict[str, Any]:
    binding = build_openharness_sdk_binding(workspace_path)
    return binding.export_sdk_binding(
        module_path,
        profile=profile,
        strict=strict,
        include_validation=include_validation,
    )
