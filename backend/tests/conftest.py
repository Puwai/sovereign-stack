import pytest
import sys
from unittest.mock import MagicMock

# Mock django-tenants for testing
sys.modules['django_tenants'] = MagicMock()
sys.modules['django_tenants.models'] = MagicMock()
sys.modules['django_tenants.middleware'] = MagicMock()
sys.modules['django_tenants.middleware.main'] = MagicMock()
