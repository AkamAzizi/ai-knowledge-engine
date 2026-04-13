---
title: "The Twelve-Factor App"
type: source
tags: [twelve-factor, saas, cloud, deployment, configuration, microservices, devops]
created: 2026-04-13
updated: 2026-04-13
sources: []
---

**Author:** Adam Wiggins (with Heroku contributors)
**Published:** ~2012, maintained as living document
**Origin:** [[entities/heroku|Heroku]]
**Raw source:** `raw/the-twelve-factor-app.md`

## Summary

The Twelve-Factor App is a methodology for building SaaS applications that are portable, deployable on modern cloud platforms, and scalable without changes to tooling or architecture. It distills operational lessons from hundreds of Heroku-deployed apps into twelve principles organized around one central idea: eliminate implicit coupling between the application and its execution environment by making all variable inputs (config, services, processes) explicit and injectable. The methodology predates containers but precisely defines the contract that makes apps container-friendly — every Kubernetes pod model follows twelve-factor patterns.

## Key Points

- **Central principle:** Eliminate implicit coupling — everything that varies between environments must be explicit and injectable; the app should be a pure function of its codebase and explicit inputs
- **Config in environment (III):** Credentials, hostnames, and per-deploy values belong in environment variables, never in checked-in files — the litmus test: can the repo be open-sourced without compromising credentials?
- **Stateless processes (VI):** No sticky sessions; all persistent state lives in a backing service (database, Redis); processes are disposable and interchangeable
- **Build/Release/Run separation (V):** Code cannot change at runtime; every change requires a new build → new release; releases are immutable and versioned
- **Port binding (VII):** The app is self-contained; it declares its webserver as a dependency and binds to a port at startup — no runtime injection of Apache or Tomcat
- **Disposability (IX):** Fast startup + graceful SIGTERM shutdown; crash-only design; enables rapid scaling and zero-downtime deploys
- **Dev/prod parity (X):** Close the time gap (hours not weeks), personnel gap (devs deploy what they write), and tools gap (same DB in dev and prod)
- **Logs as event streams (XI):** The app writes to stdout; log routing and storage are infrastructure concerns, not application concerns
- **Twelve-factor predates containers but defines their contract:** Docker, Kubernetes, and Heroku all assume twelve-factor apps; the factors are the implicit interface between apps and platforms

## Entities

- [[entities/heroku|Heroku]] — cloud platform company; origin of the Twelve-Factor methodology

## Concepts

- [[concepts/twelve-factor-app|Twelve-Factor App]] — full methodology introduced by this source
- [[concepts/cicd-pipelines|CI/CD Pipelines]] — build/release/run separation (Factor V) is the conceptual foundation of CI/CD pipeline stages
- [[concepts/modular-architecture|Modular Architecture]] — twelve-factor apps align with microservice principles; each service should independently follow all twelve factors
- [[concepts/secure-coding|Secure Coding]] — Factor III (config in environment) is a direct security practice: credentials never in source code

## Contradictions

None with existing knowledge. The twelve-factor methodology extends and formalizes practices described in [[concepts/cicd-pipelines|CI/CD Pipelines]] and [[concepts/modular-architecture|Modular Architecture]].

## Questions

- Which factors are most commonly violated in practice, and what failure modes do they cause?
- How does the twelve-factor model adapt when the "app" is a serverless function or an ML model serving endpoint?
- Factor VI (stateless processes) conflicts with models that maintain in-memory caches for performance — what is the pragmatic line?
