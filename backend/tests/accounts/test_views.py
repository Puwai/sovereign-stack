from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('accounts:register')
        self.login_url = reverse('accounts:login')
        self.valid_user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'password_confirm': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User'
        }

    def test_register_user_success(self):
        response = self.client.post(self.register_url, self.valid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.data['username'], 'testuser')

    def test_register_user_password_mismatch(self):
        invalid_data = self.valid_user_data.copy()
        invalid_data['password_confirm'] = 'differentpass'
        response = self.client.post(self.register_url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_login_user_success(self):
        # First create a user
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        # Then try to login
        login_data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.data['user']['username'], 'testuser')

    def test_login_user_invalid_credentials(self):
        login_data = {
            'username': 'nonexistent',
            'password': 'wrongpass'
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
