# Context: Health App

## Purpose
This app provides a simple health check endpoint to verify that the backend is running correctly.

## Responsibilities
- Expose a /health/ endpoint that returns the application status
- Provide basic diagnostic information about the application

## Key Components / Structure
- `views.py`: Contains the HealthCheckView that handles health check requests
- `urls.py`: Defines the URL pattern for the health check endpoint
- `apps.py`: App configuration

## Interfaces
- REST API endpoint at /api/health/ that returns JSON status information

## Dependencies
- Django

## Invariants
- The health check endpoint should always be accessible
- The endpoint should return a consistent JSON response format

## Testing Strategy
- Unit tests for the HealthCheckView
- Integration tests to verify the endpoint is accessible

## ADR Links
- [ADR-0001: Architecture Baseline & Rebuild Principles](../../adr/2024-06-04-architecture-baseline-and-rebuild-principles.md)
