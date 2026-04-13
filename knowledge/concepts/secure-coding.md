---
title: "Secure Coding"
type: concept
tags: [security, encryption, access-control, input-validation, privacy, best-practices, cryptography, obfuscation]
created: 2026-04-13
updated: 2026-04-13
sources: [coding-best-practices-and-guidelines, oligo-secure-coding-best-practices]
---

# Secure Coding

## Definition

The process of writing software that is safe from security vulnerabilities and resilient against attacks. Involves adhering to best practices, formal standards, and a security mindset throughout the entire software lifecycle. Security must be built in from the start — retrofitting it is significantly harder, and no amount of careful coding fully replaces [[concepts/runtime-security|runtime monitoring]] once deployed.

## How It Works

### Input Sanitization
The most common attack vector. Validate *and* sanitize — validation checks if input is acceptable; sanitization modifies potentially harmful input into a safe form.
- Context-aware: what's safe for a SQL query differs from HTML rendering.
- **SQL injection** — use parameterized queries + input escaping.
- **XSS** — escape special HTML characters (`<`, `>`, `"`).
- **Command injection** — neutralize metacharacters (`&`, `|`, `;`).
- Use established libraries: OWASP Java Encoder, Microsoft AntiXSS, or language-specific equivalents.
- Centralize sanitization logic to reduce inconsistency.

### Least Privilege
Users and code operate with the minimum permissions needed to perform their tasks.
- DB connections read-only where appropriate.
- Microservices get limited API access.
- Application components run as non-root users.
- System-level controls: AppArmor, SELinux.
- Secrets scoped tightly; delivered just-in-time via HashiCorp Vault or AWS IAM roles.
- Regularly audit and remove unnecessary permissions; eliminate privilege escalation paths.

### Cryptographic Practices
Cryptography only works if applied correctly — misconfigurations can nullify its protections entirely.

| Use Case | Algorithm |
|---|---|
| Symmetric encryption | AES |
| Asymmetric encryption | RSA or ECC |
| Hashing | SHA-256 or SHA-3 |
| Data in transit | TLS 1.3 |
| Service-to-service | Mutual TLS or token-based auth |

- Use vetted libraries: OpenSSL, libsodium, Bouncy Castle. Do not write custom cryptographic code.
- Generate keys with CSPRNGs (Cryptographically Secure Pseudo-Random Number Generators).
- Never expose keys in source code, logs, or environment variables.
- Use secure key management systems for key storage.

### Code Obfuscation
Disguises code logic without affecting behavior — increases the cost of reverse engineering.
- Most relevant for client-side JavaScript and mobile binaries (Android/iOS) where IP or access tokens may be exposed.
- Techniques: rename classes/variables to meaningless identifiers; hide control flow; encrypt strings decrypted only at runtime; virtualization-based obfuscation (custom virtual instruction set).
- Does not eliminate decompilation risk — must be combined with runtime protection, anti-tampering checks, and secure back-end APIs.

### Data Protection
- **Data minimization** — collect only what the project needs; delete what's no longer required.
- **Encryption at rest and in transit** — see Cryptographic Practices above.
- **Access control** — role-based permissions (RBAC); regular audits.
- **No hardcoded credentials** — never embed passwords, API keys, or secrets in source code or config files. Use environment variables or secrets managers (Vault, AWS Secrets Manager).

### Authentication & Authorization
- Multi-factor authentication for sensitive systems.
- Principle of least privilege applied to user roles (see above).
- Separate authentication (who are you?) from authorization (what can you do?).
- Avoid hardcoding credentials or sensitive info in code or config.

### Dependency Management
- Third-party libraries inherit their vulnerabilities. Keep dependencies updated.
- Audit for known CVEs — link code ownership to CVE alerts via GitHub CODEOWNERS.
- Prefer security-focused, actively maintained libraries.

### Ongoing Practices
- Regular **penetration testing** and red teaming — think like an attacker.
- **Vulnerability assessments** — systematic review for known weakness patterns.
- **Security-focused code reviews** — use OWASP/CERT checklists.
- Instrument CI/CD with exploit simulation (fuzzing, mutation testing, symbolic execution).
- Pre-commit hooks for secrets detection (gitleaks, talisman).
- Stay current: threat actors update tactics constantly; runtime monitoring bridges the gap.

## Formal Standards

See [[concepts/security-standards|Security Standards]] for full treatment.

| Standard | Scope |
|---|---|
| OWASP | Language-agnostic; web/app security checklists |
| CERT | Language-specific (C, C++, Java); vulnerability-focused rules |
| NIST SP 800-53/218 | Federal-grade; full SDLC traceability |
| ISO/IEC 27001 C-8.28 | Organizational ISMS; certification-oriented |

## Key Sources

- [[sources/coding-best-practices-and-guidelines|Coding Best Practices and Guidelines]] — surface-level security overview; data minimization, encryption, access control, input validation
- [[sources/oligo-secure-coding-best-practices|Oligo: Secure Coding Top 7]] — deep technical treatment; adds obfuscation, least privilege mechanics, specific crypto algorithms, standards, runtime security

## Related Concepts

- [[concepts/runtime-security|Runtime Security]] — the necessary complement to static secure coding; monitors behavior in production
- [[concepts/vulnerability-types|Common Vulnerability Types]] — buffer overflows, integer overflows, format strings, race conditions
- [[concepts/security-standards|Security Standards]] — OWASP, CERT, NIST, ISO 27001
- [[concepts/code-review|Code Review & Refactoring]] — security is a primary target of code review
- [[concepts/test-driven-development|Test-Driven Development]] — security testing is a specialized testing discipline
- [[concepts/code-documentation|Code Documentation]] — security-sensitive sections require heavy documentation

## Open Questions

- How do static analysis tools (Bandit for Python, Semgrep, Snyk) automate detection of insecure patterns?
- At what scale does a security type wrapper library (`SafeSQL`, `SafeHTML`) become worth building?
- OWASP Top 10 vs CERT rules — which is more actionable for a Python/data engineering context?
- What is practice #6 in the Oligo "Top 7"? The article appears to skip from 5 to 7.
