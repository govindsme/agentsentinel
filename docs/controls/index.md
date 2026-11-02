# Controls & Frameworks

This page organizes the **controls** an organisation can implement for AI security and
governance, mapped to leading **frameworks**. The underlying machine-readable data is in
`data/controls.json` and `data/frameworks.json`.

## Framework landscape

| Framework | Type | Best used for |
|-----------|------|---------------|
| **NIST AI RMF** | Voluntary framework | Risk-based practices across the lifecycle (Govern, Map, Measure, Manage) |
| **ISO/IEC 42001** | Management system standard | Certifiable AI management system (AIMS) and governance |
| **OWASP Top 10 for LLM Applications** | Technical baseline | Harden LLM applications against known risks |
| **OWASP Top 10 for Agentic AI** | Technical baseline | Harden agentic AI systems |
| **MITRE ATLAS** | Threat model | Enumerate adversarial techniques for AI |
| **EU AI Act** | Regulation | Meet binding obligations for EU-placed systems |

## Core controls catalog

### LLM & application security
- **Prompt-injection defense** — validate inputs, filter outputs, separate instructions from data, least-privilege tools.
- **Insecure output handling prevention** — treat model output as untrusted; encode at every boundary.
- **Unsafe plugin/scaffolding protection** — sandbox plugins, strict I/O validation.

### Agentic AI security
- **Least-privilege tool & delegated action control** — allowlists, scoped permissions, human approval gates.
- **Autonomy limiting** — constrain agent capability and document permitted actions.
- **Memory integrity** — retention controls, separation, treat memory as untrusted.

### Data governance
- **AI data governance & lineage** — provenance, licensing, integrity, PII handling.
- **Data-poisoning defense** — anomaly detection, provenance verification, untrusted-data segregation.

### Model & platform security
- **Model artifact integrity** — signed/shasum models, registry access control.
- **Abuse & extraction detection** — rate limits, query monitoring, membership detection.

### Security operations
- **AI-specific threat modeling** — apply MITRE ATLAS / ENISA.
- **AI security monitoring & incident response** — drift/anomaly detection, AI incident plan.

### Governance & assurance
- **AI inventory** — catalog all AI systems and models.
- **AI risk assessment** — evaluate likelihood/impact per risk tier.
- **Vendor & procurement assessment** — assess AI suppliers.
- **Control audit & evidence collection** — traceable, auditable evidence.

## Selecting controls

Use the **risk register** as the input: for each risk, one or more controls from this catalog
should reduce likelihood or impact to an acceptable residual level. Map each control to an
owner, evidence, and verification method (see [AI Risk Assessment Template](../resources/ai-risk-assessment.md)).

## Search this catalog

Use the site search (top-right) to find controls by framework, domain, or risk. For
cross-framework mappings, see [Control Crosswalks](crosswalks.md).

## References

- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [ISO/IEC 42001](https://www.iso.org/standard/81230.html)
- [OWASP GenAI Security](https://genai.owasp.org/)
- [MITRE ATLAS](https://atlas.mitre.org/)
