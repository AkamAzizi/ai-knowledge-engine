---
title: "State Management"
type: concept
tags: [state-management, architecture, mobile, react-native, flutter, redux, bloc]
created: 2026-04-13
updated: 2026-04-13
sources: [mobile-app-best-practices-2025]
---

# State Management

## Definition

A system for managing the data an application depends on at any given moment — user inputs, server responses, UI state (loading, error, success), authentication status, etc. Without a deliberate strategy, state scatters across components, producing inconsistent UI, unpredictable behavior, and difficult debugging.

## How It Works

### Core Principles

**Single source of truth** — all shared state lives in one place. Any component that needs it reads from the same source; no local copies that can drift out of sync.

**Unidirectional data flow** — state changes flow in one direction: action → state update → UI re-render. Predictable, traceable, testable.

**Immutable state** — never mutate state directly. Create a new state object with updated values. Prevents unforeseen side effects and makes change tracking trivial.

### Keep State Local When Possible
Not all state needs to be global. Start local; only elevate to shared/global state when multiple distinct components need to read or modify the same data. Over-globalizing state creates unnecessary complexity.

### Patterns and Tools by Platform

| Platform | Simple apps | Complex apps |
|---|---|---|
| React Native | Component `useState` | Redux, Zustand, MobX |
| Flutter | `setState`, `@State` | Bloc, Provider, Riverpod |
| SwiftUI | `@State`, `@ObservedObject` | `@EnvironmentObject`, custom stores |
| Android (Kotlin) | `ViewModel` + `LiveData` | MVI with StateFlow |

**Redux** (React Native) — popularized by Facebook; strict unidirectional flow; actions → reducers → new state. Verbose but highly predictable. Used by Reddit, Twitter.

**Bloc** (Flutter) — Business Logic Component; separates UI from business logic via streams of events and states. Used by Google Ads, eBay Motors.

### State Management and Architecture
State management is closely tied to [[concepts/modular-architecture|modular architecture]] patterns:
- **MVVM** — ViewModel holds and exposes state; View observes and renders; Model provides data.
- **MVI** — Model-View-Intent; user intents trigger state transformations; View is a pure function of state.
- **Clean Architecture** — UI, business logic, and data layers fully decoupled; state flows between layers through defined interfaces.

## Key Sources

- [[sources/mobile-app-best-practices-2025|Mobile App Best Practices 2025]] — covers state management patterns in mobile context (Redux, Bloc, MVVM)

## Related Concepts

- [[concepts/modular-architecture|Modular Architecture]] — state management patterns are part of the broader architectural decision; MVVM/MVI/Clean Architecture define how state flows between layers
- [[concepts/performance-optimization|Performance Optimization]] — good state management prevents unnecessary UI re-renders, directly improving performance
- [[concepts/test-driven-development|Test-Driven Development]] — decoupled state logic (separate from UI) is far easier to unit test

## Open Questions

- How do state management patterns differ between mobile and frontend web (React) contexts?
- When does Redux's verbosity justify the tradeoff over lighter alternatives like Zustand?
- How does state management interact with offline-first app design?
