# Context: Infrastructure

## Purpose
This folder contains infrastructure configurations for deploying and running the OurMoney.Africa application in various environments.

## Responsibilities
- Define Docker configurations for containerizing the application
- Set up docker-compose for local development
- Provide deployment manifests for staging and production (to be created)
- Manage environment-specific configurations

## Key Components / Structure
- `docker/`: Docker-related files
- `docker/Dockerfile.backend`: Dockerfile for the Django backend
- `docker/Dockerfile.frontend`: Dockerfile for the React frontend
- `docker/docker-compose.yml`: Docker Compose configuration for local development
- Future folders for staging and production configurations

## Interfaces
- Docker CLI for building and running containers
- docker-compose CLI for managing multi-container applications
- Environment variables for configuration

## Dependencies
- Docker Engine
- Docker Compose
- PostgreSQL Docker image
- Python and Node.js base images

## Invariants
- All services should be able to communicate with each other within the Docker network
- Environment variables should be used for configuration rather than hardcoded values
- Volumes should be used for persistent data storage
- Ports should be properly exposed for development and production

## Testing Strategy
- Test Docker builds to ensure all dependencies are correctly installed
- Verify that services start correctly with docker-compose
- Test data persistence with volumes
- Validate environment variable configuration

## ADR Links
- [ADR-0001: Architecture Baseline & Rebuild Principles](../adr/2024-06-04-architecture-baseline-and-rebuild-principles.md)
