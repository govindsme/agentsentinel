# Update History

Chronological record of site changes. The authoritative machine-readable history is in
`data/update-history.json`.

## 2026-11-02 — v1.0.0 (First Run)

- **Mode:** first_run
- **Summary:** Initial build of the Agent Sentinel AI security and governance knowledge site.
  Established the information architecture, structured data records, governance templates,
  automated validation, and GitHub Pages deployment.
- **Scope:**
  - Added AI security domain pages (GenAI/LLM, agentic AI, governance, risk, privacy, model/data/platform, supply chain).
  - Added threats, controls, and cross-framework mappings.
  - Added regulations pages (EU AI Act, NIST AI RMF, ISO/IEC 42001, jurisdiction matrix).
  - Added vulnerability index and records.
  - Added AI inventory and risk assessment templates, glossary, and sources.
  - Established `data/` structured records.
  - Configured GitHub Pages deployment and automated validation.

## 2026-11-04 — v1.1.0 (Incremental Reconciliation)

- **Mode:** incremental
- **Summary:** Delta reconciliation since the 2026-11-02 cut-off. Reconciled first-run
  metadata (the v1.0.0 first run was complete and validated).
- **Scope (changes):**
  - **Vulnerabilities (added):** `VULN-AGENT-MCP-AUTH-RCE` (Langflow MCP auth bypass & RCE,
    CVE-2026-93680 / CVE-2026-110186), `VULN-AI-CODE-SANDBOX-ESCAPE` (Prefab/Beta9 sandbox
    escape, CVE-2026-120338 / CVE-2026-120307), `VULN-AGENT-TOCTOU-WORKSPACE` (Claude Code
    edit-tool TOCTOU, CVE-2026-88968).
  - **Regulations (updated):** EU AI Act timeline per the **Digital Omnibus on AI**
    (Regulation (EU) 2026/1744) — high-risk Annex III moves to 2027-12-02, Annex I regulated
    products to 2028-08-02; new Article 5 prohibitions and watermarking deadlines.
  - **Frameworks (updated):** OWASP GenAI **LLM Top 10 2026** and OWASP **Agentic Top 10 2026**
    rankings (Excessive Agency → LLM03; Hidden Context Exposure replaces System Prompt Leakage).
  - **Claims/sources:** added Digital Omnibus, OWASP 2026, and vulnerability advisory sources/claims.
  - **Metadata:** advanced research & vulnerability cut-offs to 2026-11-04.

---
See [Research State](research-state.md) for current cut-offs and [Run Reports](run-reports.md) for run outcomes.
