# Context: Accounts App

## Purpose
This app handles user authentication, authorization, and organization management in our multi-tenant system.

## Responsibilities
- Manage user accounts and profiles
- Handle organization (tenant) creation and management
- Implement multi-tenancy at the database schema level
- Provide authentication and authorization mechanisms

## Key Components / Structure
- `models.py`: Defines User, Organization, and Domain models
- `admin.py`: Admin interface configuration for our models
- `apps.py`: App configuration

## Interfaces
- Django admin interface for managing users and organizations
- Authentication system for user login/logout
- Tenant middleware for routing requests to the correct organization schema

## Dependencies
- Django
- django-tenants

## Invariants
- Every user belongs to one or more organizations
- Each organization has its own isolated database schema
- User authentication is handled securely with Django's built-in auth system

## Testing Strategy
- Unit tests for User and Organization models
- Integration tests for multi-tenancy functionality
- Authentication flow tests

## ADR Links
- [ADR-0001: Architecture Baseline & Rebuild Principles](../../adr/2024-06-04-architecture-baseline-and-rebuild-principles.md)
