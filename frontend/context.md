# Context: Frontend

## Purpose
This folder contains the React frontend for OurMoney.Africa, providing a modern user interface for our financial cockpit.

## Responsibilities
- Provide a responsive web interface for users
- Implement authentication flows (login, registration)
- Display financial data and dashboards
- Handle user interactions and form submissions
- Communicate with the backend API

## Key Components / Structure
- `src/`: Main source code directory
- `src/pages/`: Page components (Home, Login, Register)
- `src/components/`: Reusable UI components (to be created)
- `src/services/`: API service layer (to be created)
- `src/hooks/`: Custom React hooks (to be created)
- `src/utils/`: Utility functions (to be created)
- `public/`: Static assets (to be created)
- `package.json`: Project dependencies and scripts
- `vite.config.js`: Vite configuration

## Interfaces
- REST API endpoints exposed by the backend
- User interactions through forms and UI elements
- Browser storage for tokens and user preferences

## Dependencies
- React 18+
- React Router DOM for navigation
- Vite for build tooling
- ESLint for code quality

## Invariants
- All components should be functional components using hooks
- Strict mode should be enabled in development
- All API calls should go through a service layer
- Forms should have proper validation

## Testing Strategy
- Unit tests for components using Jest and React Testing Library
- Integration tests for page flows
- End-to-end tests for critical user journeys

## ADR Links
- [ADR-0001: Architecture Baseline & Rebuild Principles](../adr/2024-06-04-architecture-baseline-and-rebuild-principles.md)
