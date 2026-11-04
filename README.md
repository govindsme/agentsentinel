# Agent Sentinel

**AI Security & Governance Reference** · _v1.1.0_

🌐 **Live static site:** <https://govindsme.github.io/agentsentinel/>

Agent Sentinel is a continuously maintained, evidence-based knowledge site covering AI
security, agentic AI, AI governance, AI risk management, privacy, regulations, control
frameworks, and newly discovered AI-related vulnerabilities.

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and deployed to
**GitHub Pages** via GitHub Actions.

## Content areas

- **AI Security Domains** — GenAI/LLM, agentic AI, governance, risk, privacy, model/data/platform, supply chain
- **Threats & Controls** — threat landscape, control catalog, cross-framework mappings
- **Regulations & Standards** — EU AI Act, NIST AI RMF, ISO/IEC 42001, jurisdiction matrix
- **Vulnerabilities** — AI vulnerability records with applicability and remediation guidance
- **Governance Resources** — AI inventory and AI risk assessment templates, glossary, sources
- **Research & Change** — research state, update history, run reports

## Repository layout

```text
docs/     Markdown content for the site (mkdocs)
          └─ resources/  AI inventory & risk assessment template pages
data/     Machine-readable structured records (JSON)
templates/  Downloadable assets (e.g., AI inventory CSV)
scripts/  Validation and build automation
reports/runs/  Per-run research reports
.github/  GitHub Pages deployment workflow
```

## Local development

```bash
# Install (isolated)
pipx install --include-deps mkdocs-material

# Validate data + links, then build
./scripts/build.sh

# Serve locally with live reload
mkdocs serve
```

## Versioning

This repository follows **Semantic Versioning** (SemVer). The current version is **v1.1.0**.
Functional changes advance **major**/**minor**/**patch** accordingly; see
[Update History](docs/research/update-history.md).

> **What's new in v1.1.0:** Adds new agentic/MCP AI vulnerabilities discovered since the
> 2026-11-02 cutoff (Langflow, Prefab UI, Claude Code, MCPhantom supply-chain), reflects the
> EU AI Act **Digital Omnibus on AI** (Regulation (EU) 2026/1744) timeline, and incorporates
> the **OWASP GenAI LLM Top 10 2026** and **OWASP Agentic Top 10 2026** rankings.

## Disclaimer

Reference and learning material. Not legal advice.
