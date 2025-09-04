# Context: OurMoney.Africa Sovereign Stack

## Purpose
This project is a complete rebuild of OurMoney.Africa, creating Africa's sovereign financial cockpit. It aims to serve 100M+ entrepreneurs across diverse African markets with a clean, systematic, and well-documented system.

## Responsibilities
- Provide a unified financial management platform
- Support multi-tenancy with schema-based separation
- Implement secure authentication and authorization
- Enable extensibility for Africa-wide payment integrations
- Maintain strict code quality and documentation standards

## Key Components / Structure
- `backend/`: Django + DRF backend with modular apps
- `frontend/`: React + TypeScript frontend
- `docs/`: Project documentation including PRD and ADRs
- `adr/`: Architecture Decision Records
- `ops/`: Infrastructure and deployment configurations
- `templates/`: Documentation templates
- `tools/`: Utility scripts for validation and maintenance

## Interfaces
- REST APIs for frontend communication
- Database interfaces for data persistence
- External payment gateway integrations (to be implemented)

## Dependencies
- Python 3.11+
- Django 5.x
- Django REST Framework
- PostgreSQL
- Node.js 18+
- React 18+

## Invariants
- Every module must have a context.md file
- Every architectural decision must have an ADR
- All code must pass type checking and tests
- No direct database queries outside of ORM

## Testing Strategy
- Unit tests for all models, serializers, and views
- Integration tests for API endpoints
- End-to-end tests for critical user flows
- Continuous integration with automated testing

## ADR Links
- [ADR-0001: Architecture Baseline & Rebuild Principles](adr/2024-06-04-architecture-baseline-and-rebuild-principles.md)
