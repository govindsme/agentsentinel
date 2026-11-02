# AI Supply Chain Security

Modern AI systems are assembled from **foundation models**, **training and fine-tuning
data**, **libraries**, **plugins**, **managed APIs**, and **infrastructure** provided by
third parties. Each link is a potential point of compromise, poisoning, or dependency risk.

## The AI supply chain

| Component | Risk examples |
|-----------|---------------|
| Foundation models | Trojaning/backdooring before distribution; counterfeit or tampered models |
| Pre-trained weights | Tampered or malicious model files |
| Training / fine-tuning data | Data poisoning; licensed/PII content without rights |
| ML libraries & packages | Known CVEs; malicious packages; dependency confusion |
| Plugins & integrations | Malicious plugins; insecure plugin interfaces |
| Managed model APIs | Undisclosed data retention; service availability; provider lock-in |
| Hardware / accelerators | Counterfeit or compromised silicon |

## Managing AI supply chain risk

### 1. Inventory third-party components
- Maintain a registry of **model providers**, **data sources**, and **dependencies**.
- Record versions, licensing, security posture, and support status.

### 2. Assess suppliers
- Apply AI-specific procurement criteria: security, transparency, data handling, availability, and exit strategy.
- Send structured **security questionnaires** and review provider security docs (e.g., SOC 2, AI-specific control reports).

### 3. Verify artifacts
- Verify **model provenance** and **signed/shasum** model artifacts before deployment.
- Use a model registry with integrity controls to prevent tampered-artifact deployment.

### 4. Apply dependency hygiene
- Track CVEs against all ML libraries and components (SBOM).
- Monitor for **package name confusion / typosquatting** and restrict source registries.

### 5. Plan for resilience
- Document **exit strategy** and data portability for managed-model dependencies.
- Establish **fallback** model options for critical functionality.

## Procurement checklist

- [ ] Supplier inventory and risk tier defined
- [ ] AI-specific security questionnaire completed
- [ ] Data-handling and retention terms confirmed
- [ ] Model provenance & integrity verification defined
- [ ] Dependency/SBOM and CVE monitoring in place
- [ ] Exit strategy and data portability agreed

## Verification

- **SBOM review** — confirm component inventory is current and scanned.
- **Artifact integrity test** — confirm deployed models match verified signatures.
- **Supplier assessment completion** — confirm all critical suppliers assessed.
- **CVE scan run** — confirm ML dependencies scanned on a cadence.

## References

- [OWASP Top 10 for LLM Applications - LLM05 Supply Chain](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-generative-ai-profile)
