---
title: "Security Standards"
type: concept
tags: [security, owasp, cert, nist, iso27001, compliance, standards]
created: 2026-04-13
updated: 2026-04-13
sources: [oligo-secure-coding-best-practices]
---

# Security Standards

## Definition

Formal frameworks and guidelines that define secure software development practices. Adopted by organizations to ensure consistent, auditable security across the development lifecycle. Four major standards are widely referenced in the industry.

## How It Works

### OWASP Secure Coding Practices
- **Origin:** Open Web Application Security Project — open, community-driven.
- **Scope:** Language-agnostic; designed for agile and traditional dev environments.
- **Core principle:** Defense in depth — multiple overlapping security controls.
- **Covers:** Input validation, authentication, access control, session management, error handling, cryptographic practices.
- **Tool:** [OWASP Secure Coding Practices Quick Reference Guide](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) — checklist format.
- **Also:** OWASP Top 10 (most critical web application risks) widely cited in [[concepts/code-review|code reviews]].

### CERT Coding Standards
- **Origin:** Software Engineering Institute, Carnegie Mellon University.
- **Scope:** Language-specific — C, C++, Java.
- **Core principle:** Determinism, predictability, fail-safe design.
- **Covers:** Buffer overflows, resource leaks, race conditions, integer issues.
- **Structure:** Each rule categorized by severity, likelihood, and remediation cost — enables risk-based prioritization.
- **Integration:** Works alongside static analysis tools and formal verification.

### NIST SP 800-53 / SP 800-218 (SSDF)
- **Origin:** National Institute of Standards and Technology (US federal).
- **Scope:** Full SDLC — requirements, design, implementation, testing.
- **Core principle:** Traceability — security requirements tracked from conception to deployment.
- **Covers:** Minimizing attack surface, privilege separation, least privilege, regular code analysis.
- **Context:** Required for federal agencies and critical infrastructure; widely adopted beyond government.
- **SP 800-218** = Secure Software Development Framework (SSDF) — the more developer-facing publication.

### ISO/IEC 27001 Control 8.28
- **Origin:** International Organization for Standardization / IEC.
- **Scope:** Organizational policy — secure coding as part of an Information Security Management System (ISMS).
- **Covers:** Code complexity, input handling, dependency management; requires developer training, code reviews, security testing.
- **Context:** International standard; used for certification across industries. Control 8.28 specifically mandates secure coding principles within the broader 27001 framework.

## Comparison

| Standard | Scope | Audience | Strength |
|---|---|---|---|
| OWASP | Web/app, language-agnostic | Developers | Practical checklists, community-driven |
| CERT | Language-specific (C/C++/Java) | Developers | Granular per-language rules with risk ratings |
| NIST | Full SDLC, federal-grade | Orgs + developers | Traceability, regulatory alignment |
| ISO 27001 | Organizational ISMS | Management + developers | Certification, international recognition |

## Key Sources

- [[sources/oligo-secure-coding-best-practices|Oligo: Secure Coding Top 7]] — covers all four standards in context of secure coding

## Related Concepts

- [[concepts/secure-coding|Secure Coding]] — these standards define *what* secure coding means in practice
- [[concepts/vulnerability-types|Common Vulnerability Types]] — OWASP Top 10 and CERT rules are organized around vulnerability classes
- [[concepts/code-review|Code Review & Refactoring]] — OWASP and CERT checklists used as review guides
- [[concepts/runtime-security|Runtime Security]] — NIST advocates defense-in-depth; runtime monitoring is one layer

## Open Questions

- PCI DSS v4.0 (payments) and SOC 2 — how do they interact with these standards?
- In practice, which standard is most commonly cited for web application development teams?
