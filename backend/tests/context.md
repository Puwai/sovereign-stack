# Context: Tests

## Purpose
This folder contains all automated tests for the OurMoney.Africa backend, ensuring code quality, functionality, and security.

## Responsibilities
- Unit tests for models, serializers, and views
- Integration tests for API endpoints
- End-to-end tests for critical user flows
- Performance and load tests (to be added later)
- Security tests (to be added later)

## Key Components / Structure
- `accounts/`: Tests for the accounts app
- `conftest.py`: pytest configuration and fixtures (if needed)
- `pytest.ini`: pytest configuration file

## Interfaces
- pytest command-line interface for running tests
- Django testing framework for database transactions and client testing
- Coverage.py for measuring code coverage

## Dependencies
- pytest
- pytest-django
- pytest-cov

## Invariants
- All tests must pass before code can be merged
- Test coverage should be maintained at a high level
- Tests should be fast and reliable
- Tests should not depend on external services without proper mocking

## Testing Strategy
- Unit tests for individual functions and methods
- Integration tests for API endpoints and database interactions
- End-to-end tests for critical user flows
- Regular coverage reports to monitor test quality

## ADR Links
- [ADR-0001: Architecture Baseline & Rebuild Principles](../adr/2024-06-04-architecture-baseline-and-rebuild-principles.md)
