import assert from "node:assert/strict";

import {
  buildHarnessAwareAgent,
  DEFAULT_MODULE_PATH,
  exportBinding,
  harnessValidate,
  loadHarnessBinding,
} from "./main.js";

async function main(): Promise<void> {
  const binding = await exportBinding(DEFAULT_MODULE_PATH, "default", true);
  const { workspacePath, registration, transport } = loadHarnessBinding(binding);
  const built = buildHarnessAwareAgent(registration, transport, workspacePath);

  assert.equal(binding.binding.binding_type, "sdk-shell");
  assert.equal(binding.transport.kind, "process");
  assert.equal(registration.tool_name, "harness_validate");
  assert.ok(typeof registration.agent_context_injection === "string" && registration.agent_context_injection.length > 0);
  assert.ok(typeof registration.skill_snippet === "string" && registration.skill_snippet.length > 0);

  const result = await harnessValidate(
    {
      module_path: DEFAULT_MODULE_PATH,
      profile: "default",
      strict: true,
    },
    transport,
    workspacePath,
  );

  assert.equal(result.status, "success");
  assert.ok(Array.isArray(result.stage_trace));
  assert.ok(typeof result.rendered_text === "string" && result.rendered_text.length > 0);
  assert.ok(result.context && typeof result.context === "object");
  assert.equal(typeof built.agent.run, "function");

  console.log("[PASS] openharness_app smoke passed");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
