# AI Security Overview

AI security is the discipline of protecting AI systems—their **data**, **models**,
**applications**, **platforms**, and **supply chains**—and managing the **risks** the
systems themselves introduce to the organisation.

## Why AI security differs from traditional security

AI systems expand the attack surface in distinctive ways:

- **Dynamic behavior**: models produce non-deterministic outputs that must be treated as untrusted.
- **Indirect input paths**: content from documents, web pages, and tools is consumed as instructions.
- **Opacity**: model behavior is difficult to fully predict or audit.
- **Extended supply chain**: foundation models, fine-tuning data, and managed platforms add third parties.
- **High-impact autonomy**: agentic systems can take actions, not just generate content.

## Core security domains

| Domain | Focus |
|--------|-------|
| [Generative AI & LLM Security](genai-llm-security.md) | Prompt injection, output handling, LLM-specific risks |
| [Agentic AI Security](agentic-ai-security.md) | Tool poisoning, excessive agency, delegation, autonomy |
| [AI Governance & Responsible AI](ai-governance.md) | Accountability, policy, trust, lifecycle governance |
| [AI Risk Management & Assurance](ai-risk.md) | Risk assessment, assurance evidence, audit |
| [AI Privacy & Data Protection](ai-privacy.md) | Personal data handling, DPIA, rights |
| [Model, Data & Platform Security](model-data-platform-security.md) | Attack surface of models, data, and infrastructure |
| [AI Supply Chain Security](ai-supply-chain.md) | Third-party model and component risk |

## The AI lifecycle security view

Security controls span the full AI lifecycle:

1. **Design** — threat modeling, privacy-by-design, risk framing
2. **Data** — provenance, integrity, PII handling
3. **Build / train** — model hardening, poisoning defense
4. **Deploy / operate** — monitoring, drift, incident response
5. **Govern** — inventory, accountability, audit

## Key references

- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP GenAI Security](https://genai.owasp.org/)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [ENISA AI Threat Landscape](https://www.enisa.europa.eu/publications/artificial-intelligence-threat-landscape)
