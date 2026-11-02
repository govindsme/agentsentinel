# Model, Data & Platform Security

Securing the AI **model**, the **data** that trains and serves it, and the **platform**
that hosts and runs it. This is the technical foundation beneath application and
governance controls.

## Model security

Attacks against the model itself:

| Attack | Description | Mitigation |
|--------|-------------|------------|
| Data poisoning | Malicious training data alters behavior | Provenance, integrity, anomaly detection |
| Backdooring | Trigger-based hidden behavior | Poison filters, behavior re-validation |
| Model inversion | Reconstruct training data from outputs | Output perturbation, access control |
| Model extraction | Steal model via queries | Rate limits, monitoring, distillation resistance |
| Evasion | Adversarial perturbations defeat inputs | Adversarial training, input validation |

## Data security

Protecting the data used to build, serve, and monitor AI:

- **Provenance & lineage** — know where every dataset came from.
- **Integrity** — detect tampering of training and serving data.
- **Classification** — label personal, sensitive, and regulated data.
- **Access control** — least privilege on data stores (object storage, vector DBs, lakehouses).
- **At-rest & in-transit encryption** — data stores, model files, and pipelines.
- **Secrets hygiene** — no credentials in code, configs, or prompts.

## Platform security

Securing the infrastructure that runs models and applications:

- **MLOps / inference pipelines** — secure CI/CD for models; signed model artifacts.
- **Model registry** — access control and versioning; prevent tampered-artifact deployment.
- **GPU/inference environments** — hardened images, sandboxing, resource isolation.
- **Vector / retrieval stores** — access control and encryption; treat retrieved content as untrusted.
- **Logging & monitoring** — capture prompt/response and model metadata for detection.
- **API security** — authentication, rate limiting, quota, and abuse detection on inference endpoints.

## Agent runtime security

Where agents execute, secure the runtime boundary:
- Sandbox code execution and browser automation.
- Isolate agent credentials with **scoped**, **short-lived** permissions.
- Apply **resource quotas** and **iteration/loop limits**.

## Verification

- **Artifact signing check** — confirm model artifacts are signed and registry-protected.
- **IAM review** — verify least privilege on all data and model infrastructure.
- **Poison/extraction tests** — run detection and abuse simulation tests.
- **Encryption audit** — confirm encryption for data and model files at rest and in transit.

## References

- [NIST Adversarial Machine Learning (AI 100-2e2025)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
