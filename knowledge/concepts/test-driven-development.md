---
title: "Test-Driven Development"
type: concept
tags: [testing, tdd, unit-tests, error-handling, python, mobile, testing-pyramid, best-practices]
created: 2026-04-13
updated: 2026-04-13
sources: [coding-best-practices-and-guidelines, mobile-app-best-practices-2025]
---

# Test-Driven Development

## Definition

A software development methodology where tests are written *before* the code they validate. The cycle is: write a failing test → write the minimum code to pass it → refactor. Ensures every piece of code is validated from the start.

## How It Works

### TDD Cycle
1. Write a test for a piece of functionality that doesn't exist yet (it will fail).
2. Write the minimum code to make the test pass.
3. Refactor the code while keeping tests green.

### Unit Tests
Tests that validate individual functions or components in isolation. Tools in Python: `unittest` (standard library) and `pytest` (third-party, more ergonomic).

```python
import unittest

def square(x):
    return x ** 2

class TestSquare(unittest.TestCase):
    def test_square_positive_number(self):
        result = square(5)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()
```

Best practice: test with small, known-output datasets first. Then expand to edge cases.

Unit tests also serve as **executable documentation** — they show how a function is meant to be called and what it should return.

### try-except Blocks
For runtime errors that can't be prevented by logic alone (I/O failures, network errors, unexpected user input), `try-except` blocks provide graceful degradation:

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    result = None

print(f"Result: {result}")
```

Anticipate expected failure modes and define how the program should respond — prevents crashes and improves user experience.

### The Testing Pyramid
A structural model for balancing test investment:

```
        /\
       /  \   ← End-to-end UI tests (few, slow, expensive)
      /----\
     /      \ ← Integration tests (moderate)
    /--------\
   /          \ ← Unit tests (many, fast, cheap)
  /____________\
```

- **Unit tests** — fast, cheap, isolated; form the wide base. Run on every commit.
- **Integration tests** — verify that components work together; run on PR.
- **End-to-end / UI tests** — test complete user flows; use selectively for critical paths only (login, checkout, core features). Slow and brittle at scale.

### Mobile-Specific Testing
- **Automation frameworks:** Espresso (Android), XCTest (iOS) for automating critical user flows.
- **Real device testing** — emulators catch many bugs but miss rendering issues, hardware quirks, and performance on low-end devices. Use cloud-based device farms (BrowserStack, Firebase Test Lab, AWS Device Farm).
- **Conditions to test:** Different screen sizes, OS versions, network speeds (3G, offline mode, flaky connections).
- **Chaos engineering** — Netflix proactively tests system resilience by intentionally injecting failures.

## Key Sources

- [[sources/coding-best-practices-and-guidelines|Coding Best Practices and Guidelines]] — introduces TDD, unit tests, and try-except (Python/general context)
- [[sources/mobile-app-best-practices-2025|Mobile App Best Practices 2025]] — adds testing pyramid structure, mobile automation frameworks (Espresso, XCTest), real device and cloud testing

## Related Concepts

- [[concepts/code-review|Code Review & Refactoring]] — tests are reviewed alongside code; missing tests are a red flag
- [[concepts/code-documentation|Code Documentation]] — tests as executable documentation
- [[concepts/version-control|Version Control]] — tests run as quality gates in CI/CD on each commit/PR
- [[concepts/cicd-pipelines|CI/CD Pipelines]] — the testing pyramid maps directly to pipeline stages; unit → integration → UI as mandatory quality gates
- [[concepts/secure-coding|Secure Coding]] — security testing is a specialized form of testing
- [[concepts/tool-evaluation|Tool Evaluation]] — agent tool evals follow the same philosophy as TDD; define expected behavior first, measure, iterate

## Open Questions

- How does TDD interact with exploratory data analysis — does it make sense in a notebook context?
- What coverage percentage is "enough"?
- Property-based testing (Hypothesis library) as a complement to example-based unit tests?
- How do you test offline-mode behavior and flaky network conditions reliably?
