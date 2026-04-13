---
title: "User-Centric Design"
type: concept
tags: [ux, design, user-research, usability-testing, prototyping, product]
created: 2026-04-13
updated: 2026-04-13
sources: [mobile-app-best-practices-2025]
---

# User-Centric Design

## Definition

A design methodology that places the end-user at the center of every decision. Rather than building what developers or stakeholders assume users want, it discovers what users actually need — through research, persona development, journey mapping, and iterative usability testing before and after launch.

## How It Works

### The Process

```
User research → Personas + journeys → Wireframes/prototypes → Usability testing → Build → Analytics → Repeat
```

Each stage informs the next. The loop never ends — post-launch analytics feed back into new research cycles.

### 1. User Research
- **When:** Before a single line of code is written.
- **Methods:** User interviews, surveys, contextual inquiry.
- **Goal:** Understand real pain points, goals, and behaviors — not assumptions.
- Continue research throughout development to validate new assumptions as they emerge.

### 2. User Personas
Fictional but data-grounded representations of user archetypes. Capture: goals, frustrations, device habits, context of use. Keeps design decisions anchored to real user types rather than abstract "users."

### 3. User Journey Mapping
Visualize the full sequence of steps a user takes to accomplish a goal — including emotional state, friction points, and drop-off risks. Reveals problems that feature lists alone never surface.

### 4. Prototyping and Usability Testing
- Build interactive prototypes in **Figma** (design) or **Maze** (usability testing) before development begins.
- Test with real target users — observe where they struggle, hesitate, or get confused.
- Identify friction and fix it at prototype stage — far cheaper than post-development changes.

### 5. Post-Launch Analytics Loop
After launch, close the feedback loop with quantitative + qualitative data:
- **Quantitative:** Time-on-task, funnel drop-off, error rates, retention (via Firebase Analytics or equivalent).
- **Qualitative:** App store reviews, in-app feedback surveys, support tickets.
- Combine both: numbers tell you *where* the problem is; qualitative tells you *why*.

### What Good UCD Produces
- Higher user retention and engagement.
- Reduced support burden (fewer confused users).
- Features validated before expensive development.
- Accessibility improvements built in from the start (larger touch targets, readable fonts — also a mobile-first benefit).

Examples: Duolingo — continuous usability testing on gamification elements to measure what actually motivates users. Slack — interface continuously refined through user feedback.

## Key Sources

- [[sources/mobile-app-best-practices-2025|Mobile App Best Practices 2025]] — primary treatment of user-centric design in mobile context

## Related Concepts

- [[concepts/mobile-first-design|Mobile-First Design]] — mobile-first determines constraints; user-centric design determines how to meet user needs within those constraints
- [[concepts/analytics-and-monitoring|Analytics and Monitoring]] — the quantitative half of the post-launch feedback loop
- [[concepts/tool-evaluation|Tool Evaluation]] — user-centric design's "test with real users" philosophy mirrors the agent tool evaluation approach: measure real behavior, not assumed behavior

## Open Questions

- How do you run effective remote usability testing compared to in-person sessions?
- At what prototype fidelity do usability tests produce the most useful signal?
- How does user-centric design interact with accessibility standards (WCAG)?
