# AI Risk Management & Assurance

AI risk management is the disciplined process of **identifying, assessing, treating,
and monitoring** the risks posed by and to AI systems across their lifecycle.

## Distinguish AI risk from classic IT risk

AI adds novel risk drivers:

- **Model risk** — incorrect, biased, or unstable predictions.
- **Security risk** — adversarial attacks on data, models, and agents.
- **Autonomy risk** — unintended high-impact or irreversible agent actions.
- **Data & privacy risk** — personal and regulated data handling.
- **Compliance risk** — evolving regulation (EU AI Act, GDPR, sector rules).
- **Reputational & societal risk** — harmful outputs, deepfakes, misinformation.

## A practical AI risk process

### 1. Framing & inventory
- Define AI risk appetite and use-case boundaries.
- Enumerate all AI systems (see [AI Inventory Template](../resources/ai-inventory.md)).

### 2. Risk assessment
- Evaluate likelihood and impact for each identified risk.
- Categorise by tier (e.g., EU AI Act risk tiers, internal criticality).
- Use the [AI Risk Assessment Template](../resources/ai-risk-assessment.md).

### 3. Treatment
- Avoid, mitigate, transfer, or accept each risk.
- Map treatment to concrete controls (see [Controls & Frameworks](../controls/index.md)).
- Identify owners and deadlines.

### 4. Monitoring & review
- Monitor controls operation, model drift, and emerging threats.
- Re-assess on material change or at a defined cadence.

### 5. Assurance & evidence
- Collect, retain, and trace **evidence** for every control.
- Support internal audit, third-party assessment, and regulator review.

## Aligning to frameworks

| Framework | Role in risk management |
|-----------|-------------------------|
| **NIST AI RMF** | Core risk-management process (Govern, Map, Measure, Manage) |
| **ISO/IEC 42001 & 23894** | Certifiable AIMS and AI-specific risk guidance aligned to ISO 31000 |
| **EU AI Act** | Mandatory risk-management system for high-risk systems (Art. 9) |
| **GDPR** | DPIA and data-protection risk for personal data |

## Assurance: from risk to auditable evidence

A strong risk program produces a **traceable chain**:

```
Policy/Appetite → Risk Register → Control Mapping → Operating Evidence → Audit Opinion
```

Every risk should be traceable to a control, and every control to evidence of operation.

## Get started

Build inventory and risk assessments using the provided templates:
- [AI Inventory Template](../resources/ai-inventory.md)
- [AI Risk Assessment Template](../resources/ai-risk-assessment.md)

## References

- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [ISO/IEC 42001](https://www.iso.org/standard/81230.html)
- [ISO/IEC 23894](https://www.iso.org/standard/77304.html)
