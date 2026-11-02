# Control Crosswalks

Cross-framework mappings help map controls, risks, and obligations between leading
frameworks and regulations. The full machine-readable mapping is in `data/control-crosswalks.json`.

## EU AI Act ↔ NIST AI RMF

Operationalize EU AI Act obligations using NIST AI RMF practices.

| EU AI Act | NIST AI RMF |
|-----------|-------------|
| Risk management system (Art. 9) | Govern & Manage |
| Data governance (Art. 10) | Map - data lifecycle |
| Technical documentation (Art. 11) | Govern - documentation & transparency |
| Human oversight (Art. 14) | Manage - human-AI teaming |
| Accuracy, robustness, cybersecurity (Art. 15) | Measure & Manage |
| Transparency (Art. 13) | Govern - transparency & accountability |

## OWASP Top 10 for LLM ↔ MITRE ATLAS

Map technical risk categories to adversarial techniques for testing and detection.

| OWASP LLM risk | MITRE ATLAS |
|----------------|-------------|
| LLM01 Prompt Injection | Initial Access, Execution, Collection, Exfiltration |
| LLM02 Insecure Output Handling | Execution, Impact |
| LLM04 Tool Poisoning | ML Attack Staging |
| LLM09 Sensitive Information Disclosure | Exfiltration, Collection |

## ISO/IEC 42001 ↔ NIST AI RMF

Use ISO/IEC 42001 as a certifiable management-system wrapper for AI RMF practices.

| ISO/IEC 42001 | NIST AI RMF |
|---------------|-------------|
| AI management system (AIMS) | Govern |
| Risk assessment (clause 10.4 / Annex B) | Map & Measure |
| Operational controls / AI risk treatment | Manage |
| Measurement & evaluation (clause 9) | Measure |

## OWASP Top 10 (Web) ↔ OWASP Top 10 for LLM

Classic web risks re-expressed as LLM-specific risk categories.

| OWASP Web 2021 | OWASP LLM |
|----------------|-----------|
| Injection (A03) | LLM01 Prompt Injection |
| Sensitive Data Exposure (A02) | LLM09 Sensitive Information Disclosure |
| Security Misconfiguration (A05) | LLM06 / LLM08 Excessive Agency |
| Insecure Design (A04) | LLM05 Supply-Chain, LLM02 Output Handling |

## Using crosswalks

1. Identify your **source framework** (the obligation or framework you must meet).
2. Use the mapping to find the **target framework** you already operationalize.
3. Confirm each mapped control has an **owner** and **evidence**.
4. Record any gaps where a target-framework control is absent.
