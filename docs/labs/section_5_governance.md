# Section 5 Lab - Governance

## What you will practice
- Masking as a guardrail.
- Prompt-injection and malicious-input defenses.
- Licensing and legal-risk review.
- Mitigation for problematic source text.

## Exercises
1. Mask sensitive values in `data/raw/policies/policy_manual.md` with `mask_sensitive_text()`.
2. Test `looks_malicious()` with injection attempts.
3. Create a licensing checklist for internal documents, third-party web data, and purchased content.
4. Recommend how to handle toxic, private, or low-quality text before it reaches the vector index.

## Check yourself
- Did you explain performance tradeoffs of masking?
- Did you identify both prevention and remediation guardrails?
- Did you connect data governance to legal risk reduction?
