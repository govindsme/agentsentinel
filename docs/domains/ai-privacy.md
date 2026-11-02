# AI Privacy & Data Protection

AI systems process—and often **learn from, memorise, or disclose**—personal data at
unprecedented scale. Privacy teams must govern how AI handles personal, sensitive, and
regulated data across the full lifecycle.

## AI-specific privacy risks

- **Data ingestion** — training and fine-tuning on personal data without purpose limitation.
- **Data retention** — raw data persisted for model improvement beyond legitimate use.
- **Memorisation & extraction** — models reproduce memorised personal data in outputs.
- **Sensitive disclosure** — RAG or generation surfaces personal/sensitive information.
- **Automated decisions** — profiling and decisions with legal or significant effects.
- **De-identification failure** — "de-identified" data re-identifiable through models.
- **Inference** — models infer sensitive attributes not in the original data.

## Privacy-by-design for AI

1. **Data minimisation** — collect and retain only what is necessary.
2. **Purpose limitation** — define and constrain permitted uses, including model training.
3. **Access control** — restrict access to training data, retrieval sources, and model APIs.
4. **Redaction & filtering** — scrub PII from inputs and outputs; filter sensitive output.
5. **Retention & deletion** — enforce retention schedules and support erasure.
6. **De-identification** — apply modern techniques; verify resistance to reconstruction.

## Privacy impact assessment (DPIA)

Conduct a DPIA when AI processes personal data at scale, uses new technology, or makes
automated decisions with significant effects (GDPR Art. 35).

**A DPIA for AI should cover:**

- Description of the AI processing and personal data involved.
- Necessity and proportionality assessment.
- Risk to individuals (including bias, exclusion, and privacy harm).
- Mitigations (technical and organisational).
- Where applicable, high-risk findings for the Data Protection Authority (DPA).

## Governance obligations

Align AI data practices with:
- **GDPR** — lawfulness, purpose limitation, data minimisation, accuracy, storage limitation,
  integrity/confidentiality, accountability, and individual rights.
- **EU AI Act** — data governance requirements for high-risk systems.
- **Sector rules** — health, financial, and regulated-industry data requirements.

## Verification

- **Data lineage review** — confirm each dataset's source, purpose, and retention.
- **Output redaction tests** — verify PII scrubbing and sensitive-output filtering.
- **Extraction/membership checks** — test for memorisation of personal data.
- **DPIA register** — confirm DPIAs exist and are current for qualifying systems.

## References

- [GDPR (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-generative-ai-profile)
