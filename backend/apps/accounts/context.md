# Context: Accounts App

## Purpose
This app handles user authentication, authorization, and organization management in our multi-tenant system.

## Responsibilities
- Manage user accounts and profiles
- Handle organization (tenant) creation and management
- Implement multi-tenancy at the database schema level
- Provide authentication and authorization mechanisms (JWT, device sessions)

## Key Components / Structure
- `models.py`: Defines User, Organization, and Domain models
- `serializers.py`: Serializers for user registration and login
- `views.py`: Views for user registration and login
- `admin.py`: Admin interface configuration for our models
- `apps.py`: App configuration
- `urls.py`: URL patterns for account-related endpoints

## Interfaces
- Django admin interface for managing users and organizations
- REST API endpoints for user registration and login
- Authentication system for user login/logout
- Tenant middleware for routing requests to the correct organization schema

## Dependencies
- Django
- django-tenants
- djangorestframework
- djangorestframework-simplejwt

## Invariants
- Every user belongs to one or more organizations
- Each organization has its own isolated database schema
- User authentication is handled securely with JWT tokens
- Passwords are properly hashed and validated

## Testing Strategy
- Unit tests for User and Organization models
- Integration tests for multi-tenancy functionality
- Authentication flow tests (registration, login, token refresh)
- API endpoint tests for registration and login views

## ADR Links
- [ADR-0001: Architecture Baseline & Rebuild Principles](../../adr/2024-06-04-architecture-baseline-and-rebuild-principles.md)
