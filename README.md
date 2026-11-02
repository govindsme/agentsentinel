# Agent Sentinel

**AI Security & Governance Reference** · _v1.0.0_

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

This repository follows **Semantic Versioning** (SemVer). The current version is **v1.0.0**.
Functional changes advance **major**/**minor**/**patch** accordingly; see
[Update History](docs/research/update-history.md).

## Disclaimer

Reference and learning material. Not legal advice.
