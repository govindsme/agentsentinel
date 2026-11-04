# Agentic AI Security

Agentic AI systems pursue goals with a degree of **autonomy**, using **tools**, **memory**,
and **delegation** to act in digital or physical environments. This introduces a new class
of security risk beyond content generation.

## What changes with agents

Unlike a chat assistant, an agent can:

- **Call tools** (APIs, code interpreters, browsers, databases).
- **Persist memory** across sessions.
- **Delegate subtasks** to other agents.
- **Act** on the environment (create, modify, delete, execute, spend).

Every capability is a new attack surface and a new path to unintended consequences.

## Top agentic AI risks (OWASP)

| Risk | Description | Primary mitigations |
|------|-------------|---------------------|
| **Tool poisoning** | Malicious or tampered tools/data alter agent behavior | Tool trust & integrity; allowlist; monitor tool output |
| **Delegation abuse** | Malicious sub-agents or delegation chains expand impact | Control delegation scope; verify sub-agent identities |
| **Excessive agency** | Agent has more capability than needed | Least privilege; autonomy limits; capability matrix |
| **Inadequate oversight** | Agent acts without human review | Human-in-the-loop; approval gates; audit logging |
| **Memory poisoning** | Manipulated or poisoned memory persist bad behavior | Memory integrity; retention controls; separation |
| **Unbounded autonomy** | Agent loops or escalates without limits | Resource quotas; iteration limits; kill switches |
| **Context manipulation** | Adversarial content steers agent decisions | Input/output validation; instruction-data separation |

## Core security principles

1. **Constrain autonomy**: define exactly what an agent may do and under what conditions.
2. **Least-privilege tools**: grant only the tools and permissions the task requires.
3. **Human-in-the-loop**: require approval for high-impact or irreversible actions.
4. **Verify and log**: audit every tool call, decision, and delegated action.
5. **Isolate**: sandbox agent execution and segregate memory and credentials.

## Securing the agent stack

- **Model**: prompt/response guards, red teaming for agent hijacking.
- **Orchestrator**: enforce the agent's permitted plan; validate tool calls against an allowlist schema.
- **Tools/APIs**: authentication, rate limiting, scoped scopes, parameter validation.
- **Memory**: encrypt at rest; apply retention/expiry; treat stored content as untrusted input.
- **Credentials**: never embed secrets in prompts; use scoped short-lived credentials.

## Verification

- **Agent tabletop tests**: simulate compromise scenarios (prompt injection leading to tool misuse).
- **Permission matrix audit**: confirm agent capability exactly matches tool grants.
- **Approval-gate tests**: verify high-impact actions require human approval.
- **Logging review**: confirm complete traceability of agent decisions and actions.

## Model Context Protocol (MCP) risk surface

MCP servers expose agent capabilities as callable tools, adding a **trust and authentication**
boundary that has become an active attack surface:

- **Unauthenticated/under-authenticated MCP endpoints** — agent frameworks exposing MCP tool
  enumeration with automatic-login defaults have allowed remote authentication bypass and
  remote code execution (e.g., Langflow CVE-2026-93680, CVE-2026-110186; fixed in 1.13.0).
- **Prompt-injected tool arguments** — crafted content can reach host command execution
  through MCP tool parameters that are interpolated into shell or code runners.
- **Agentic supply chain** — AI coding agents have been observed installing **deprecated or
  archived MCP servers** carrying unpatched, high-severity flaws (see "MCPhantom" reporting).
- **Path/sandbox escapes** — agent tools and code runners must not trust pathname validation
  divorced from file-descriptor-anchored use (e.g., Claude Code CVE-2026-88968 TOCTOU).

Follow the OWASP GenAI and OWASP Agentic 2026 guidance together: use the LLM Top 10 when the
model is a **component** of an application, and the Agentic Top 10 (ASI01–ASI10) once the model
**acts** with tools, memory, and consequences.

## References

- [OWASP GenAI Security Project](https://genai.owasp.org/)
- [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/download/52117/)
- [MITRE ATLAS](https://atlas.mitre.org/)
