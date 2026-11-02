# Vulnerability Records

Detailed machine-readable vulnerability records are maintained in `data/`. This page
synthesizes them for reference. For the authoritative status, see
[Vulnerability State](../index.md) and `data/vulnerability-state.json`.

## VULN-LLM01-PROMPT-INJECTION — Critical

- **Category:** LLM Application · **CWE:** CWE-94 / CWE-77 · **Baseline CVSSv4:** 9.3
- **Description:** Manipulating LLMs via crafted inputs to change behavior, including
  indirect injection through tools or documents, enabling data exfiltration or unintended actions.
- **Affected scope:** LLM prompt handling, agent tool interfaces, RAG/context loading.
- **Remediation:** Input/output sanitization; instruction-data separation; least-privilege
  tool access; output filtering; human review for high-impact actions.
- **Aliases:** prompt injection, indirect prompt injection, ChatGPT prompt injection.

## VULN-LLM02-INVALID-OUTPUT — High

- **Category:** LLM Application · **CWE:** CWE-79 / CWE-94 / CWE-78 · **Baseline CVSSv4:** 8.5
- **Description:** Treating LLM output as trusted without validation, leading to XSS,
  command injection, or unsafe downstream action.
- **Affected scope:** Front-end rendering, downstream consumers, agent actions from output.
- **Remediation:** Validate, encode, and sanitize all LLM outputs; treat output as untrusted.
- **Aliases:** insecure output handling, LLM02.

## VULN-EXCESSIVE-AGENCY — Critical

- **Category:** Agentic AI · **CWE:** CWE-863 · **Baseline CVSSv4:** 9.0
- **Description:** Agentic systems granted excessive autonomy, privilege, or tool access
  leading to unintended high-impact or irreversible actions.
- **Affected scope:** Agent orchestration, tool/API integrations, delegation chains, memory stores.
- **Remediation:** Limit autonomy; least-privilege tools; human approval gates; document permitted actions.
- **Aliases:** excessive agency, over-privileged agent, delegation abuse.

## VULN-DATA-POISONING — High

- **Category:** Model / Supply Chain · **CWE:** CWE-501 · **Baseline CVSSv4:** 8.5
- **Description:** Adversarial manipulation of training data to backdoor, bias, or degrade model behavior.
- **Affected scope:** Training datasets, fine-tuning pipelines, embedding/vector stores.
- **Remediation:** Dataset provenance & integrity; anomaly detection; poisoned-data filtering; re-evaluation.
- **Aliases:** training data poisoning, backdoor attack.

## VULN-MODEL-EXTRACTION — High

- **Category:** Model Security · **CWE:** CWE-200 · **Baseline CVSSv4:** 7.5
- **Description:** Query-based reconstruction of model behavior or extraction of memorized training data.
- **Affected scope:** Model inference APIs, hosted foundation models.
- **Remediation:** Rate limiting; query monitoring; membership attack detection; access control.
- **Aliases:** model stealing, model inversion, membership inference.

## VULN-SENSITIVE-DISCLOSURE — High

- **Category:** Privacy / LLM · **CWE:** CWE-200 · **Baseline CVSSv4:** 8.0
- **Description:** Model or application discloses personal, sensitive, or regulated data via outputs or retrieval.
- **Affected scope:** LLM outputs, RAG retrieval sources, training data.
- **Remediation:** Data minimization; output redaction/filtering; retrieval access controls; DPIA.
- **Aliases:** sensitive information disclosure, LLM09.

## Related records

These records are maintained in repo `data/` files. For the consolidated view see the
[Vulnerability Index](../index.md), and for status see `data/vulnerability-state.json`:
- **Products** — component applicability (`data/vulnerability-products.json`)
- **Aliases** — aliases and tracking names (`data/vulnerability-aliases.json`)
- **History** — event timeline per record (`data/vulnerability-history.json`)
- **Remediation** — actionable remediation register (`data/remediation-actions.json`)

## Process notes

- Provider advisories **without CVEs** are tracked (common for model-provider issues).
- **Aliases** added after initial publication are reconciled on each run.
- Discovered/updated records are reflected in [Run Reports](../../research/run-reports.md).
