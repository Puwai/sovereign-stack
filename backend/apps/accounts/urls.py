from django.urls import path
from .views import RegisterView, LoginView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # Add more account-related URLs here as needed
]
