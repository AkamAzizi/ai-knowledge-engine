---
title: "Twelve-Factor App"
type: concept
tags: [twelve-factor, saas, cloud, deployment, configuration, processes, portability]
created: 2026-04-13
updated: 2026-04-13
sources: [the-twelve-factor-app]
---

# Twelve-Factor App

## Definition

The Twelve-Factor App is a methodology for building SaaS applications that are portable, deployable on modern cloud platforms, and scalable without changes to tooling or architecture. Its central principle: **eliminate implicit coupling between the app and its execution environment** by making everything that varies between environments (config, services, processes) explicit and injectable.

## How It Works

The methodology defines twelve constraints grouped around the central principle:

### Configuration and Dependencies
| Factor | Rule | Why |
|---|---|---|
| I. Codebase | One repo, many deploys | Enforces one-to-one app/codebase relationship |
| II. Dependencies | Declare and isolate all dependencies | No implicit system packages; `bundle install` as complete setup |
| III. Config | Store config in environment variables | Credentials never in code; litmus: can repo be open-sourced today? |
| IV. Backing Services | Treat all services as attached resources | Swap local MySQL → RDS by changing one env var; no code changes |

### Build and Run
| Factor | Rule | Why |
|---|---|---|
| V. Build/Release/Run | Strictly separate stages | Code cannot change at runtime; every change requires a new release |
| VI. Processes | Stateless, share-nothing processes | State lives in backing services; processes are interchangeable |
| VII. Port Binding | Export services via port binding | App is self-contained; no runtime injection of webserver |
| VIII. Concurrency | Scale via the process model | Add more processes; different types for web vs. workers |

### Operations
| Factor | Rule | Why |
|---|---|---|
| IX. Disposability | Fast startup, graceful shutdown | Enables rapid scaling and zero-downtime deploys |
| X. Dev/Prod Parity | Keep environments identical | Close time gap, personnel gap, and tools gap |
| XI. Logs | Treat logs as event streams | Write to stdout; routing and storage are infrastructure concerns |
| XII. Admin Processes | Run admin tasks as one-off processes | Same release/config as production; dependency isolation applies |

## Most Commonly Violated in Practice

**Factor III (Config in environment):** Hardcoded credentials or environment-specific constants in code is the most common violation — and a direct security risk per [[concepts/secure-coding|Secure Coding]] principles.

**Factor VI (Stateless processes):** Applications that rely on in-process caches, local file system, or sticky sessions are tightly coupled to specific instances and cannot scale horizontally.

**Factor X (Dev/prod parity):** Using SQLite in development against PostgreSQL in production is the classic violation — subtle behavioural differences cause production-only bugs.

## Why This Matters for Modern Infrastructure

The twelve factors predate containers but precisely define what makes apps container-friendly:
- **Docker:** A Dockerfile implements factors I, II, V by packaging the codebase and its dependencies into a build artifact
- **Kubernetes:** The pod model assumes stateless (VI), port-bound (VII), disposable (IX) processes
- **CI/CD:** Build/release/run separation (V) is the conceptual foundation of CI/CD pipeline stages — see [[concepts/cicd-pipelines|CI/CD Pipelines]]
- **Microservices:** Each service in a microservice architecture should independently satisfy all twelve factors

## Key Sources

- [[sources/the-twelve-factor-app|Wiggins / Heroku]] — original methodology; drawn from experience of hundreds of Heroku-deployed apps

## Related Concepts

- [[concepts/cicd-pipelines|CI/CD Pipelines]] — Factor V (build/release/run) is the CI/CD foundation; Factor IX (disposability) enables rolling deploys
- [[concepts/modular-architecture|Modular Architecture]] — each module/microservice should be an independent twelve-factor app
- [[concepts/secure-coding|Secure Coding]] — Factor III (config in environment) is a security requirement; credentials in source code is a critical vulnerability
- [[concepts/performance-optimization|Performance Optimization]] — Factor VIII (concurrency via processes) and Factor IX (disposability) enable horizontal scaling strategies

## Open Questions

- How does the twelve-factor model apply to serverless functions — do factors like port binding still make sense?
- Factor VI (stateless) conflicts with performance optimizations that rely on in-memory caches — where is the pragmatic line?
- What is the minimal viable twelve-factor compliance for a monolith migrating to microservices?
