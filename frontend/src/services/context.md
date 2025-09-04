# Context: Services

## Purpose
This folder contains service classes that handle communication with the backend API and manage application state.

## Responsibilities
- Make HTTP requests to backend endpoints
- Handle authentication tokens (storage, retrieval, refresh)
- Process API responses and errors
- Provide a consistent interface for components to interact with backend data

## Key Components / Structure
- `authService.js`: Handles user authentication (registration, login, logout)
- Future services for other API endpoints (to be created as needed)

## Interfaces
- JavaScript/TypeScript functions that return Promises
- localStorage for token storage (consider more secure alternatives in production)

## Dependencies
- Fetch API for HTTP requests
- localStorage for client-side storage

## Invariants
- All API calls should be wrapped in try/catch blocks
- Errors should be properly handled and propagated to calling components
- Tokens should be stored securely (consider httpOnly cookies in production)
- Service methods should be stateless and reusable

## Testing Strategy
- Unit tests for each service method
- Mock HTTP requests to test different response scenarios
- Integration tests with the actual backend (in controlled environments)

## ADR Links
- [ADR-0001: Architecture Baseline & Rebuild Principles](../../../adr/2024-06-04-architecture-baseline-and-rebuild-principles.md)
