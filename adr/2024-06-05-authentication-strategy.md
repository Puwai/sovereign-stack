# ADR 2024-06-05: Authentication Strategy

## Status
Accepted

## Context
The OurMoney.Africa system requires a secure, scalable authentication mechanism that supports:
- User registration and login
- JWT-based token authentication
- Refresh token rotation for security
- Multi-tenancy awareness
- Device session tracking (for future implementation)

We need to choose an authentication approach that is both secure and easy to implement.

## Decision
We will implement authentication using:
1. **djangorestframework-simplejwt**: A mature, well-maintained JWT implementation for Django REST Framework.
2. **Standard JWT flow**: Access tokens with short lifetime (60 minutes) and refresh tokens with longer lifetime (7 days).
3. **Token rotation**: Refresh tokens will be rotated after each use, with blacklisting of old tokens.
4. **DRF integration**: Use DRF's authentication classes to automatically handle token validation.
5. **Custom serializers**: Implement custom serializers for registration and login to handle validation and user creation.

## Consequences
- Provides a secure, industry-standard authentication mechanism
- Supports token refresh for long-lived user sessions
- Integrates well with Django REST Framework
- Allows for future extension with device session tracking
- Requires careful handling of token storage on the frontend
