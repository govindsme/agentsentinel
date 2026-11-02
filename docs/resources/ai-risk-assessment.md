# AI Risk Assessment Template

Use this template to assess the risks of a single AI system and document the control
mapping and evidence needed for assurance. Pair it with the
[AI Inventory Template](ai-inventory.md).

## 1. System identification

- **System ID:** `AI-___`
- **System / Product name:**
- **Owner (business / technical):**
- **System type:** Application / Agent / Model / Embedded
- **Deployment model:** Cloud / on-prem / SaaS / self-hosted
- **Models & providers:**
- **Data processed & sensitivity:**
- **Date of assessment:**

## 2. Regulatory classification

- **EU AI Act tier:** Prohibited / High-risk / GPAI / Limited (transparency) / Minimal
- **GDPR applicability:** Personal data? Sensitive data? Automated decisions? → **DPIA required?**
- **Sector obligations:** Health / financial / public / other

## 3. Risk assessment

Score **Likelihood (1-5)** and **Impact (1-5)** per risk; calculate **Risk = L × I**.

| # | Risk / threat | Likelihood | Impact | Risk score | Existing controls | Residual risk |
|---|---------------|-----------|--------|------------|-------------------|---------------|
| 1 | Prompt injection | | | | | |
| 2 | Insecure output handling | | | | | |
| 3 | Excessive agency (if agent) | | | | | |
| 4 | Data poisoning (if trained) | | | | | |
| 5 | Sensitive info disclosure | | | | | |
| 6 | Model/training data extraction | | | | | |
| 7 | Compliance / bias / privacy | | | | | |

## 4. Control mapping

Map each accepted/mitigated risk to a control and evidence.

| Risk | Control | Control owner | Verification method | Evidence ref |
|------|---------|---------------|---------------------|--------------|
| | | | | |

## 5. Risk treatment decisions

- [ ] Avoid — discontinue the use case
- [ ] Mitigate — implement additional controls
- [ ] Transfer — insure / contract
- [ ] Accept — residual risk approved by owner

**Residual risk approval (signature / role / date):**

## 6. Assurance & evidence

List the evidence artefacts that attest to each control's **design** and **operation**:

- Red-team / injection test results
- Output-boundary test results
- Permission matrix / autonomy audit
- Data lineage & provenance records
- DPIA reference
- Monitoring & incident logs

## 7. Review cadence

- **Next review date:**
- **Trigger for ad-hoc review:** material change in model, data, scope, or regulation.

## Related resources

- [AI Risk Management & Assurance](../domains/ai-risk.md)
- [Controls & Frameworks](../controls/index.md)
- [Regulatory Landscape](../regulations/index.md)
