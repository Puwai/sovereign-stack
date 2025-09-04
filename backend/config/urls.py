"""
OurMoney.Africa URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.health.urls')),  # Add our health check endpoint
    path('api/accounts/', include('apps.accounts.urls')),  # Add our accounts endpoints
    # Add our app URLs here as we create them
]
