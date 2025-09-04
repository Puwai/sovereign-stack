# Context: Backend

## Purpose
This folder contains the Django backend for OurMoney.Africa, implementing the core financial cockpit functionality with a clean, well-documented architecture.

## Responsibilities
- Handle authentication and authorization
- Manage multi-tenancy
- Provide REST APIs for frontend consumption
- Implement business logic for financial operations
- Ensure data persistence and integrity

## Key Components / Structure
- `config/`: Django configuration (settings, URLs, WSGI)
- `apps/`: Modular Django apps (to be created as needed)
- `requirements.txt`: Python dependencies

## Interfaces
- REST APIs consumed by the frontend
- Database interface for data persistence
- Authentication system for user management

## Dependencies
- Python 3.11+
- Django 5.x
- Django REST Framework
- PostgreSQL (for production)

## Invariants
- All API endpoints must be documented with OpenAPI
- All models must have proper validation
- All code must pass mypy type checking
- All functionality must have unit tests

## Testing Strategy
- Unit tests for models and serializers
- Integration tests for API endpoints
- End-to-end tests for critical flows

## ADR Links
- [ADR-0001: Architecture Baseline & Rebuild Principles](../adr/2024-06-04-architecture-baseline-and-rebuild-principles.md)
