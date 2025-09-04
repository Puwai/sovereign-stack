from django.contrib.auth.models import AbstractUser
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    """
    # Add any additional fields specific to OurMoney users here
    # For example:
    # phone_number = models.CharField(max_length=15, blank=True)
    # profile_picture = models.URLField(blank=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class Organization(TenantMixin):
    """
    Organization represents a tenant in our multi-tenant system.
    Each organization has its own schema in the database.
    """
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    # Add any additional fields specific to organizations here

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    """
    Domain model for organizations.
    """
    pass
