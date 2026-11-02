# AI Inventory Template

Maintain a comprehensive catalog of every AI system, model, and use case in the
organisation. The **AI inventory is the foundation** of governance, risk assessment,
and compliance.

Use this template to record one row per AI system or model. Adapt fields to your
organisation.

## Template

| # | Field | Description | Example |
|---|-------|-------------|---------|
| 1 | System ID | Unique identifier | AI-001 |
| 2 | System / Product name | Business name | "Support Copilot" |
| 3 | Use case description | What it does | Summarizes support tickets |
| 4 | Business owner | Responsible function | Support Operations |
| 5 | Technical owner | Responsible technical team | Platform Engineering |
| 6 | System type | Application / Agent / Model / Embedded | Agentic assistant |
| 7 | Model / provider | Foundation model + provider | GPT-4o (OpenAI) |
| 8 | Deployment model | Cloud / on-prem / SaaS / self-hosted | SaaS (API) |
| 9 | Data processed | Data types & sensitivity | Support transcripts (PII) |
| 10 | Data sources | Training / retrieval sources | CRM, KB, tickets |
| 11 | Risk tier | EU AI Act tier / internal tier | High-risk (prohibited/high/limited/minimal) |
| 12 | Key risks | Top risks identified | Prompt injection, data leakage |
| 13 | Compliance obligations | EU AI Act / GDPR / sector | GDPR DPIA required |
| 14 | Status | In design/dev/prod/decommissioned | In production |
| 15 | Last risk review | Date of last assessment | 2026-11-02 |
| 16 | Evidence link | Link to risk assessment evidence | /assessments/AI-001 |

## Excel / CSV column set

```csv
System ID,System Name,Use Case,Business Owner,Technical Owner,System Type,Model/Provider,Deployment Model,Data Processed,Data Sources,Risk Tier,Key Risks,Compliance Obligations,Status,Last Risk Review,Evidence Link
AI-001,Support Copilot,Summarizes support tickets,Support Ops,Platform Eng,Agentic assistant,GPT-4o (OpenAI),SaaS (API),Support transcripts (PII),CRM;KB;tickets,High-risk,Prompt injection;data leakage,GDPR DPIA,In production,2026-11-02,/assessments/AI-001
```

## Related resources

- [AI Risk Assessment Template](ai-risk-assessment.md) — assess each inventoried system.
- [AI Governance](../domains/ai-governance.md) — governance program guidance.
- [Controls & Frameworks](../controls/index.md) — controls to apply per system.
