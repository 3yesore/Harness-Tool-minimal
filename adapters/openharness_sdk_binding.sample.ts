// OpenHarness SDK binding sample
// This sample uses the real OpenHarness Agent API and a narrow Python process transport.

import { execFile } from "node:child_process";
import { promisify } from "node:util";
import { tool, type LanguageModel } from "ai";
import { z } from "zod";
import { Agent } from "@openharness/core";

const execFileAsync = promisify(execFile);

type HarnessValidateArgs = {
  module_path: string;
  profile?: string;
  strict?: boolean;
};

type BindingRegistration = {
  tool_definition: Record<string, unknown>;
  context_payload: Record<string, unknown>;
  provider_hints: Record<string, unknown>;
  middleware_hints: Record<string, unknown>;
  agent_context_injection: string;
  skill_snippet: string;
  tool_call_example: Record<string, unknown>;
};

type BindingTransport = {
  kind: "process";
  python_command: string;
  script_path: string;
};

export function loadHarnessBinding(
  registration: BindingRegistration,
  transport: BindingTransport,
  workspacePath: string,
) {
  return { registration, transport, workspacePath };
}

async function harnessValidate(
  args: HarnessValidateArgs,
  transport: BindingTransport,
  workspacePath: string,
) {
  const python = process.env.PYTHON ?? transport.python_command ?? "python";
  const cliArgs = [
    transport.script_path,
    "--workspace-path",
    workspacePath,
    "--module-path",
    args.module_path,
    "--profile",
    args.profile ?? "default",
  ];
  if (args.strict) cliArgs.push("--strict");

  const { stdout } = await execFileAsync(python, cliArgs, { cwd: workspacePath });
  return JSON.parse(stdout);
}

export function buildHarnessAwareAgent(
  model: LanguageModel,
  registration: BindingRegistration,
  transport: BindingTransport,
  workspacePath: string,
) {
  const { registration: loadedRegistration, transport: loadedTransport, workspacePath: loadedWorkspacePath } =
    loadHarnessBinding(registration, transport, workspacePath);

  const harnessValidateTool = tool({
    description: "Run Harness Tool validation as a preflight contract gate.",
    inputSchema: z.object({
      module_path: z.string(),
      profile: z.string().default("default"),
      strict: z.boolean().default(false),
    }),
    execute: async (args: HarnessValidateArgs) => harnessValidate(args, loadedTransport, loadedWorkspacePath),
  });

  const agent = new Agent({
    name: "harness-aware-agent",
    model,
    systemPrompt: [
      loadedRegistration.agent_context_injection,
      "",
      loadedRegistration.skill_snippet,
    ].join("\n"),
    tools: {
      harness_validate: harnessValidateTool,
    },
    maxSteps: 20,
  });

  return {
    agent,
    contextPayload: loadedRegistration.context_payload,
    providerHints: loadedRegistration.provider_hints,
    middlewareHints: loadedRegistration.middleware_hints,
    toolCallExample: loadedRegistration.tool_call_example,
  };
}
