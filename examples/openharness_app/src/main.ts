import { execFile } from "node:child_process";
import assert from "node:assert/strict";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { promisify } from "node:util";

import { openai } from "@ai-sdk/openai";
import { tool } from "ai";
import { Agent } from "@openharness/core";
import { z } from "zod";

import type { BindingExport, BindingRegistration, BindingTransport, HarnessValidateArgs } from "./types.js";

const execFileAsync = promisify(execFile);

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const EXAMPLE_ROOT = path.resolve(__dirname, "..");
const REPO_ROOT = path.resolve(EXAMPLE_ROOT, "..", "..");

export const DEFAULT_MODULE_PATH = "examples/local_extension";
export const DEFAULT_PROFILE = "default";

export function resolvePythonCommand(): string {
  return process.env.PYTHON ?? "python";
}

export async function exportBinding(
  modulePath = DEFAULT_MODULE_PATH,
  profile = DEFAULT_PROFILE,
  strict = true,
): Promise<BindingExport> {
  const python = resolvePythonCommand();
  const scriptPath = path.join(REPO_ROOT, "scripts", "openharness_sdk_binding_export.py");
  const args = [
    scriptPath,
    "--workspace-path",
    REPO_ROOT,
    "--module-path",
    modulePath,
    "--profile",
    profile,
  ];
  if (strict) args.push("--strict");
  const { stdout } = await execFileAsync(python, args, { cwd: REPO_ROOT });
  return JSON.parse(stdout) as BindingExport;
}

export function loadHarnessBinding(
  binding: BindingExport,
): {
  workspacePath: string;
  registration: BindingRegistration;
  transport: BindingTransport;
} {
  return {
    workspacePath: binding.binding.workspace_path,
    registration: binding.registration,
    transport: binding.transport,
  };
}

export async function harnessValidate(
  args: HarnessValidateArgs,
  transport: BindingTransport,
  workspacePath: string,
): Promise<Record<string, unknown>> {
  const python = process.env.PYTHON ?? transport.python_command ?? "python";
  const cliArgs = [
    path.resolve(workspacePath, transport.script_path),
    "--workspace-path",
    workspacePath,
    "--module-path",
    args.module_path,
    "--profile",
    args.profile ?? DEFAULT_PROFILE,
  ];
  if (args.strict) cliArgs.push("--strict");
  const { stdout } = await execFileAsync(python, cliArgs, { cwd: workspacePath });
  return JSON.parse(stdout) as Record<string, unknown>;
}

export function buildHarnessAwareAgent(
  registration: BindingRegistration,
  transport: BindingTransport,
  workspacePath: string,
) {
  const harnessValidateTool = tool({
    description: "Run Harness Tool validation as a preflight contract gate.",
    inputSchema: z.object({
      module_path: z.string(),
      profile: z.string().default(DEFAULT_PROFILE),
      strict: z.boolean().default(false),
    }),
    execute: async (args: HarnessValidateArgs) => harnessValidate(args, transport, workspacePath),
  });

  const agent = new Agent({
    name: "harness-aware-agent",
    model: openai("gpt-5.4"),
    systemPrompt: [registration.agent_context_injection, "", registration.skill_snippet].join("\n"),
    tools: {
      harness_validate: harnessValidateTool,
    },
    maxSteps: 20,
  });

  return {
    agent,
    harnessValidateTool,
    contextPayload: registration.context_payload,
    toolCallExample: registration.tool_call_example,
  };
}

export async function main(): Promise<void> {
  const binding = await exportBinding();
  const { workspacePath, registration, transport } = loadHarnessBinding(binding);
  const built = buildHarnessAwareAgent(registration, transport, workspacePath);

  assert.equal(binding.binding.binding_type, "sdk-shell");
  console.log("openharness_app example ready");
  console.log(`workspace: ${workspacePath}`);
  console.log(`tool: ${registration.tool_name}`);
  console.log(`agent: ${built.agent.name}`);
  console.log(`module: ${String((built.contextPayload as Record<string, unknown>).module_name ?? "unknown")}`);
}

const isDirectRun = process.argv[1] && path.resolve(process.argv[1]) === __filename;
if (isDirectRun) {
  main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
  });
}
