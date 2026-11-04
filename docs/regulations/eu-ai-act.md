# EU Artificial Intelligence Act

The **EU AI Act** (Regulation (EU) 2024/1689) is the first comprehensive, risk-based law
for AI. It entered into force on **1 August 2024** and applies in phases. It was amended
by the **Digital Omnibus on AI** (Regulation (EU) 2026/1744, in force **27 July 2026**),
which postponed several high-risk deadlines and added new prohibited practices.

!!! note "Scope"
    Applies to AI systems placed on the EU market or used in the EU, affecting providers,
    deployers, importers, distributor, and (through market scope) many non-EU organisations.

## Timeline

| Date | Milestone |
|------|-----------|
| 2024-08-01 | Act entered into force |
| 2025-02-02 | **Prohibited practices** apply; AI literacy duty (Art. 4) |
| 2025-08-02 | GPAI model obligations apply; governance & first penalties |
| 2026-08-02 | **Transparency** obligations (Art. 50) & AI Office/GPAI enforcement powers activate |
| 2026-12-02 | **Watermarking** (Art. 50(2)) for tools already on market; new **prohibitions** on AI-generated CSAM & non-consensual intimate imagery (new AI systems must watermark from first day) |
| 2027-12-02 | **High-risk** systems in listed areas (Annex III) apply *(postponed from 2026-08-02 by the Digital Omnibus)* |
| 2028-08-02 | High-risk AI embedded in **regulated products** (Annex I) apply *(postponed from 2027-08-02)* |

!!! note "2026 Digital Omnibus changes"
    Regulation (EU) 2026/1744 postponed high-risk application to **2 Dec 2027** (stand-alone,
    Annex III) and **2 Aug 2028** (embedded in regulated products, Annex I). It added new
    Article 5 prohibitions for **AI-generated child sexual abuse material** and
    **non-consensual intimate imagery** (effective 2 Dec 2026), and reduced the grace period
    for content watermarking. It did **not** change the penalty regime or the 2 Aug 2026
    transparency obligations. National **regulatory sandboxes** are delayed to 2 Dec 2027.

## Risk-based obligations

### Prohibited practices
Bans on AI practices that pose unacceptable risk (e.g., social scoring, real-time remote
biometric identification in public spaces subject to strict conditions). The Digital Omnibus
adds prohibitions on AI-generated child sexual abuse material and non-consensual intimate imagery.

### High-risk systems (Title III)
For AI systems that are a safety component of regulated products, or used in listed
high-impact areas, obligations include:

- **Risk management system** (Art. 9)
- **Data governance** (Art. 10)
- **Technical documentation** (Art. 11) & record-keeping (Art. 12)
- **Transparency** (Art. 13)
- **Human oversight** (Art. 14)
- **Accuracy, robustness, & cybersecurity** (Art. 15)
- **Conformity assessment** before placing on the market
- **Registration** in the EU database

### General-purpose AI (GPAI)
Providers of general-purpose AI models (e.g., foundation models) must meet transparency
(Art. 53) and, for models with systemic risk, additional risk-assessment obligations
(Art. 55).

### Limited transparency
AI systems that interact with humans, generate deepfakes, or generate synthetic content
carry transparency obligations (Art. 50), including watermarking/detection of AI-generated
content.

## Implementing the AI Act

Use the [crosswalk to NIST AI RMF](../controls/crosswalks.md) to operationalize obligations:

- Risk management → NIST Govern & Manage
- Data governance → Map
- Human oversight → Manage
- Cybersecurity → Measure & Manage

Conduct an **AI Act classification** for every system. See the
[AI Risk Assessment Template](../resources/ai-risk-assessment.md) and the
[evaluation methods](../references/sources.md).

## References

- [EUR-Lex: Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [EU AI Act landing](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [EU Council: AI Act timeline](https://www.consilium.europa.eu/en/policies/artificial-intelligence-act/timeline-artificial-intelligence/)
