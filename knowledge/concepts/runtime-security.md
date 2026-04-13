---
title: "Runtime Security"
type: concept
tags: [security, runtime, monitoring, production, devSecOps]
created: 2026-04-13
updated: 2026-04-13
sources: [oligo-secure-coding-best-practices]
---

# Runtime Security

## Definition

The practice of monitoring and protecting applications *during execution in production*, as opposed to static analysis which inspects code before deployment. Runtime security observes actual software behavior to detect anomalies, catch vulnerabilities that weren't caught at development time, and block exploitation in real time.

## How It Works

Static secure coding and runtime security are complementary layers:

| Layer | When | What it catches |
|---|---|---|
| Static analysis / secure coding | Before deployment | Known patterns, code smells, injection risks |
| Runtime security | During production | Missed vulnerabilities, zero-days, behavioral anomalies |

**Runtime telemetry** — data collected during execution:
- Function call traces
- Resource access logs
- User interaction patterns

This data enables **behavior-based detection**: alerting on deviations from established norms that indicate misuse or an active breach attempt.

**Key insight (Gal Elbaz):** Code that is secure today may be insecure tomorrow. New CVEs are discovered constantly. Runtime monitoring catches newly discovered vulnerabilities exploited against code that passed all static checks at release time.

### Runtime Security in CI/CD (DevSecOps)
- Pre-commit hooks (gitleaks, talisman) catch secrets and type violations before they reach the repo.
- Exploit simulation (fuzzing, mutation testing, symbolic execution) integrated into pipelines.
- Real-time feedback loops close the gap between development and security response.

### RASP (Runtime Application Self-Protection)
A class of tools that instruments application code to detect and block attacks from within. [[entities/oligo-security|Oligo Security]]'s approach is in this category — monitoring production to detect and block missed vulnerabilities.

## Key Sources

- [[sources/oligo-secure-coding-best-practices|Oligo: Secure Coding Top 7]] — introduces runtime security as a necessary complement to static secure coding

## Related Concepts

- [[concepts/secure-coding|Secure Coding]] — the static layer that runtime security complements
- [[concepts/security-standards|Security Standards]] — OWASP, NIST advocate defense-in-depth; runtime security is one layer
- [[concepts/vulnerability-types|Common Vulnerability Types]] — runtime monitoring detects exploitation attempts of these

## Open Questions

- How does RASP compare to WAF (Web Application Firewall) and SIEM in the security stack?
- What are the performance overhead trade-offs of runtime instrumentation?
- How do tools like Oligo, Sqreen, and Datadog ASM differ in approach?
