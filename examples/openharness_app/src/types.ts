export type HarnessValidateArgs = {
  module_path: string;
  profile?: string;
  strict?: boolean;
};

export type BindingRegistration = {
  tool_name: string;
  tool_definition: Record<string, unknown>;
  context_payload: Record<string, unknown>;
  agent_context_injection: string;
  skill_snippet: string;
  tool_call_example: Record<string, unknown>;
};

export type BindingTransport = {
  kind: "process";
  python_command: string;
  script_path: string;
};

export type BindingExport = {
  binding: {
    target_runtime: string;
    binding_type: string;
    host_runtime: boolean;
    workspace_path: string;
  };
  transport: BindingTransport;
  registration: BindingRegistration;
  typescript_sample: string;
  references: Record<string, string>;
};
