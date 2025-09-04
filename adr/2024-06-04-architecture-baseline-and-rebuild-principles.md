# ADR 2024-06-04: Architecture Baseline & Rebuild Principles

## Status
Accepted

## Context
The OurMoney.Africa system requires a complete rebuild to address issues in the current stack:
- Multiple broken authentication layers
- Legacy UI components
- Inconsistent code quality and testing
- Fragile deployment process

We need to establish clear principles for the rebuild to ensure we don't carry forward legacy problems.

## Decision
We will rebuild from scratch following these principles:
1. **Clean Architecture**: Start with a skeleton, enforce ADRs and context documentation in every major component.
2. **Backend-First**: Define contracts, services, and tests before touching frontend.
3. **Single Source of Truth (SSOT)**: All decisions logged in ADRs, no "tribal knowledge."
4. **Systematic Testing**: Enforce mypy, pytest, and coverage gates from day one.
5. **Strict Typing**: Python typing + TypeScript strict mode.
6. **One-Shot Stack**: Fully deployable, monitored, and tested end-to-end.

## Consequences
- Provides a solid foundation for the rebuild
- Ensures all future architectural decisions are documented
- Establishes clear quality gates for code contributions
- Creates a reference point for team alignment# ADR 2024-06-04: Architecture Baseline & Rebuild Principles

## Status
Accepted

## Context
The OurMoney.Africa system requires a complete rebuild to address issues in the current stack:
- Multiple broken authentication layers
- Legacy UI components
- Inconsistent code quality and testing
- Fragile deployment process

We need to establish clear principles for the rebuild to ensure we don't carry forward legacy problems.

## Decision
We will rebuild from scratch following these principles:
1. **Clean Architecture**: Start with a skeleton, enforce ADRs and context documentation in every major component.
2. **Backend-First**: Define contracts, services, and tests before touching frontend.
3. **Single Source of Truth (SSOT)**: All decisions logged in ADRs, no "tribal knowledge."
4. **Systematic Testing**: Enforce mypy, pytest, and coverage gates from day one.
5. **Strict Typing**: Python typing + TypeScript strict mode.
6. **One-Shot Stack**: Fully deployable, monitored, and tested end-to-end.

## Consequences
- Provides a solid foundation for the rebuild
- Ensures all future architectural decisions are documented
- Establishes clear quality gates for code contributions
- Creates a reference point for team alignment
