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

## References

- [OWASP Agentic AI - Threats and Mitigations](https://genai.owasp.org/)
- [OWASP Top 10 for Agentic AI](https://genai.owasp.org/resource/owasp-top-10-for-agentic-ai/)
- [MITRE ATLAS](https://atlas.mitre.org/)
