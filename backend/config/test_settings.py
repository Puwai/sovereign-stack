"""
Test settings for OurMoney.Africa project.
"""
from .settings import *

# Use SQLite for testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

# Use a simpler password hasher for faster tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Disable migrations for faster tests
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

# Override tenant settings for testing
TENANT_MODEL = None
TENANT_DOMAIN_MODEL = None

# Remove django-tenants from installed apps for testing
INSTALLED_APPS = [app for app in INSTALLED_APPS if app != 'django_tenants']

# Remove tenant middleware for testing
MIDDLEWARE = [mw for mw in MIDDLEWARE if 'TenantMainMiddleware' not in mw]

# Remove database routers for testing
DATABASE_ROUTERS = ()
