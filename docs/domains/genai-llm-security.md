# Generative AI & LLM Application Security

LLM applications have distinct security risks because they process untrusted input as
both **data** and **instructions**, and because their **outputs** are non-deterministic
and must be treated as untrusted.

## The OWASP Top 10 for LLM Applications

The de-facto technical baseline for securing LLM applications:

| # | Risk | Core mitigation |
|---|------|-----------------|
| LLM01 | **Prompt Injection** | Instruction/data separation; validate untrusted content; least-privilege tools |
| LLM02 | **Insecure Output Handling** | Validate/encode all model output at downstream boundaries |
| LLM03 | **Training Data Poisoning** | Provenance & integrity controls on training/fine-tuning data |
| LLM04 | **Model Denial of Service** | Rate limiting; resource quotas; guard against resource-exhaustion prompts |
| LLM05 | **Supply Chain Vulnerabilities** | Vetted model/plugin/components; SBOM; CVE monitoring |
| LLM06 | **Sensitive Information Disclosure** | Data minimization; output filtering; retrieval access control |
| LLM07 | **Insecure Plugin Design** | Sandboxing; strict I/O validation at plugin boundaries |
| LLM08 | **Excessive Agency** | Limit autonomy, permissions, and tool scope; human approval gates |
| LLM09 | **Overreliance** | AI-assisted validation; guardrails; human oversight for critical tasks |
| LLM10 | **Model Theft** | Access control, monitoring, and distillation resistance |

## Architecture security patterns

### Treat prompts as a trust boundary
- Separate **instructions** from **untrusted data** (e.g., delimiters, structured framing).
- Never concatenate user content directly into system prompts without principle of least trust.

### Treat outputs as untrusted
- Apply input-validation discipline to model output before it reaches browsers, shells, or tools.
- Guard against **indirect prompt injection** through retrieved documents (RAG).

### Protect the tool/plugin surface
- Enable tools with **least privilege** only.
- Define explicit **allowlists** of permitted tool actions.
- Add **human-in-the-loop** approval for high-impact operations.

## Testing & verification

- **Red teaming**: run adversarial prompt-injection and jailbreak tests on a regular cadence.
- **Awareness corpus**: maintain a prompt-injection test suite and regression suite.
- **Tool permission matrix**: verify the mapping of agent capability to tool permissions.
- **Output boundary checks**: test XSS/injection behavior across every output consumer.

## References

- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP GenAI Security](https://genai.owasp.org/)
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-generative-ai-profile)
- [NIST Adversarial Machine Learning (AI 100-2e2025)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf)
