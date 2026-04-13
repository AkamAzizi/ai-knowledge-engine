---
title: "Heroku"
type: entity
tags: [heroku, cloud, saas, platform, twelve-factor, deployment]
created: 2026-04-13
updated: 2026-04-13
sources: [the-twelve-factor-app]
---

# Heroku

## Overview

Heroku is a cloud platform-as-a-service (PaaS) company, acquired by Salesforce in 2010. It pioneered the modern app deployment model — git push to deploy, environment variable config, ephemeral processes — and formalized these operational patterns into the Twelve-Factor App methodology.

## Key Contributions

- **Twelve-Factor App methodology:** Authored by Adam Wiggins (Heroku co-founder) and contributors; codifies the operational lessons from hundreds of Heroku-deployed apps into twelve portable principles
- **Git-push deployment model:** The convention of deploying by pushing to a remote git repository, now standard across cloud platforms
- **Ephemeral dynos:** The process model (Factor VI, VIII, IX) — stateless, disposable, horizontally scalable units — is Heroku's core abstraction and the conceptual ancestor of Kubernetes pods
- **Config vars:** The implementation of Factor III (config in environment) — Heroku's `config:set` command made environment-variable configuration the de facto standard

## Appearances

- [[sources/the-twelve-factor-app|Wiggins / Heroku]] — Twelve-Factor App methodology

## Related

- [[concepts/twelve-factor-app|Twelve-Factor App]] — methodology originating from Heroku's operational experience
- [[concepts/cicd-pipelines|CI/CD Pipelines]] — Heroku pioneered the git-push-to-deploy model that CI/CD systems generalize
