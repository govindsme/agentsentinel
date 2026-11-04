# Vulnerability Index

This site tracks **AI-related vulnerabilities** — both classic vulnerabilities that affect
AI systems and novel AI-specific weaknesses — with applicability and remediation guidance.
The underlying machine-readable records are in `data/vulnerabilities.json` and related files.

## Active AI vulnerability records

| ID | Title | Category | Severity | Status |
|----|-------|----------|----------|--------|
| [VULN-LLM01-PROMPT-INJECTION](records/index.md) | Prompt injection | LLM Application | Critical | Active |
| [VULN-LLM02-INVALID-OUTPUT](records/index.md) | Insecure output handling | LLM Application | High | Active |
| [VULN-DATA-POISONING](records/index.md) | Data poisoning | Model / Supply Chain | High | Active |
| [VULN-MODEL-EXTRACTION](records/index.md) | Model & data extraction | Model Security | High | Active |
| [VULN-EXCESSIVE-AGENCY](records/index.md) | Excessive agency (agentic) | Agentic AI | Critical | Active |
| [VULN-SENSITIVE-DISCLOSURE](records/index.md) | Sensitive information disclosure | Privacy / LLM | High | Active |
| [VULN-AGENT-MCP-AUTH-RCE](records/index.md) | Agent framework MCP auth bypass & RCE | Agentic AI / MCP | Critical | Active |
| [VULN-AI-CODE-SANDBOX-ESCAPE](records/index.md) | AI-generated code sandbox escape | AI Application | Critical | Active |
| [VULN-AGENT-TOCTOU-WORKSPACE](records/index.md) | Agentic coding tool TOCTOU workspace escape | Agentic AI | High | Active |

## State summary

- **Total tracked:** 9 · **Active:** 9 · **Resolved:** 0
- **Critical:** 4 · **High:** 5

See [Vulnerability State](records/index.md) for the authoritative snapshot from
`data/vulnerability-state.json`.

## Remediation

Every record links to remediation actions. The consolidated remediation register is in
`data/remediation-actions.json`. Key cross-cutting actions:

- Run **periodic full reconciliation** to revalidate active records and discover new AI vulnerabilities.
- Track **provider advisories** even when a CVE is not issued (common for model-provider issues).
- Monitor **aliases** added after initial publication (see `data/vulnerability-aliases.json`).

## How to use this index

1. Find vulnerabilities applicable to your **components** (`data/vulnerability-products.json`).
2. Read the **record** for description, affected scope, and remediation.
3. Assign **ownership** and track remediation to closure.
4. Re-assess on **every site run** for newly discovered or updated vulnerabilities.

For the complete per-run discovery and assessment history, see
[Run Reports](../research/run-reports.md) and [Update History](../research/update-history.md).
