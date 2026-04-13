---
title: "Modular Architecture"
type: concept
tags: [architecture, modularity, clean-architecture, mvvm, dependency-injection, scalability]
created: 2026-04-13
updated: 2026-04-13
sources: [mobile-app-best-practices-2025]
---

# Modular Architecture

## Definition

A software architecture approach where the codebase is broken into independent, interchangeable modules — each responsible for a specific feature or layer. The opposite of a monolithic codebase where all logic is entangled. Modular architecture enables teams to grow, codebases to scale, and features to be added or replaced without cascading breakage.

## How It Works

### Core Principles

**Single responsibility per module** — each module does one thing. A payments module handles payments; it doesn't also know about user profiles.

**Clear module contracts** — modules communicate through well-defined public interfaces (APIs). Internals are hidden. This is the "contract" that prevents tight coupling and makes modules independently replaceable.

**Separation of concerns** — UI, business logic, and data access live in separate layers. A change to the database layer doesn't ripple into the UI.

**Dependency injection** — modules receive their dependencies from outside rather than creating them internally. Makes modules testable in isolation and swappable.

### Architectural Patterns

**Clean Architecture** — three concentric layers:
- **Entities** — core business logic; no external dependencies.
- **Use Cases** — application-specific logic; orchestrates entities.
- **Interface Adapters / Frameworks** — UI, databases, APIs; the outermost ring.
- Dependencies point inward only — outer layers know about inner layers, never the reverse.

**MVVM (Model-View-ViewModel)**
- **Model** — data and business logic.
- **ViewModel** — prepares and exposes data for the View; handles UI logic.
- **View** — renders UI; observes ViewModel; contains no logic.
- Common in iOS (SwiftUI, UIKit) and Android (Jetpack).

**MVI (Model-View-Intent)**
- **Intent** — user action or event.
- **Model** — immutable state.
- **View** — pure function of state; renders whatever the model says.
- Strict unidirectional flow; highly predictable; pairs naturally with [[concepts/state-management|state management]] libraries like Bloc.

### Dependency Injection Tools

| Platform | Tool |
|---|---|
| Android | Hilt, Dagger, Koin |
| iOS | Resolver, Swinject |
| Flutter | GetIt, injectable |
| React Native | InversifyJS |

### Why It Matters at Scale
- Hundreds of engineers can contribute to a single codebase without blocking each other — each team owns their module.
- New features are added in new modules, not injected into existing ones.
- Easier onboarding — new developers learn one module without needing to understand the entire system.
- Examples: Uber, Netflix — modular architectures at massive scale.

### Don't Over-Engineer
Match complexity to the problem. A simple app doesn't need Clean Architecture. Start with a foundation that can evolve; don't implement five abstraction layers for a two-screen MVP.

## Key Sources

- [[sources/mobile-app-best-practices-2025|Mobile App Best Practices 2025]] — primary treatment; Clean Architecture, MVVM, MVI, dependency injection in mobile context

## Related Concepts

- [[concepts/state-management|State Management]] — MVVM and MVI are both architectural patterns and state management strategies; they're deeply intertwined
- [[concepts/cicd-pipelines|CI/CD Pipelines]] — modular codebases build faster in CI (parallel module builds) and are safer to deploy
- [[concepts/test-driven-development|Test-Driven Development]] — modular architecture makes unit testing straightforward; each module is testable in isolation
- [[concepts/performance-optimization|Performance Optimization]] — lazy module loading can improve startup time; unnecessary dependencies between modules cause avoidable overhead

## Open Questions

- At what team/codebase size does the overhead of Clean Architecture pay off vs. MVVM alone?
- How does micro-frontend architecture relate to modular mobile architecture?
- What are the best practices for versioning module interfaces when multiple teams own different modules?
