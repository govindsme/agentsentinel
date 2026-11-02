# Threat Landscape

AI systems face a threat landscape that combines **classic** IT threats with **AI-specific**
adversarial techniques. This page uses machine-readable data from `data/threats.json`.

## Top AI threats

| Threat | Category | Typical impact | Atlas-aligned timing |
|--------|----------|----------------|----------------------|
| **Prompt injection** | LLM Security | Data exfiltration, tool misuse, privilege escalation | Initial Access → Exfiltration |
| **Tool poisoning** | Agentic AI | Unintended actions, data leakage | ML Attack Staging → Impact |
| **Data poisoning** | Model & Data | Backdoored/degraded behavior, bias | ML Attack Staging |
| **Sensitive information disclosure** | Privacy & LLM | Personal/sensitive data exposure | Collection / Exfiltration |
| **Model & data extraction** | Model Security | IP theft, training-data leakage | Exfiltration |
| **Excessive agency / delegation abuse** | Agentic AI | Privileged unintended actions | Execution / Impact |
| **Unsafe plugin/scaffolding** | LLM Security | Arbitrary code execution | Execution |

## AI-specific threat modeling (MITRE ATLAS)

ATLAS is the definitive adversarial technique knowledge base for AI systems. Use it to:

- Enumerate techniques relevant to each AI component (model, data, application, platform).
- Identify detection points for each technique.
- Build test cases and red-team plans.
- Communicate findings in a shared language.

## Event-driven classification

Classify each threat using a shared threat register that includes:

- **Threat agent** (who), **vector** (how), **asset** (what), **impact** (so what).
- **Mitigations** currently in place.
- **Residual risk** and **owner**.

## Controls

Map every threat to one or more controls. See [Controls & Frameworks](../controls/index.md)
and [Control Crosswalks](../controls/crosswalks.md).

## Detection & response

- Log model inputs/outputs and agent tool calls.
- Monitor for poisoning, extraction, and drift anomalies.
- Maintain an **AI incident response** plan with an AI-specific incident taxonomy.
- Run **tabletop exercises** for prompt-injection and agent-compromise scenarios.

## References

- [MITRE ATLAS](https://atlas.mitre.org/)
- [ENISA AI Threat Landscape](https://www.enisa.europa.eu/publications/artificial-intelligence-threat-landscape)
- [OWASP Agentic AI - Threats and Mitigations](https://genai.owasp.org/)
