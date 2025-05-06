# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Створюємо адміна з токеном
        self.admin = User.objects.create_user(
            username='admin',
            password='adminpass',
            email='admin@example.com',
            is_admin=True
        )
        self.admin_token = Token.objects.create(user=self.admin)
        
        # Створюємо звичайного користувача з токеном
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='user@example.com',
            is_admin=False
        )
        self.user_token = Token.objects.create(user=self.user)

    def test_registration(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'password': 'newpass123',
            'email': 'new@example.com',
            'is_admin': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('token', response.data)

    def test_admin_access(self):
        # Використовуємо токен для автентифікації
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token.key}')
        url = reverse('admin-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_non_admin_access(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_token.key}')
        url = reverse('admin-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)