from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_login_valid_user(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Redirection après connexion réussie
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_invalid_user(self):
        response = self.client.post(reverse('login'), {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Page de connexion rechargée
        self.assertFalse(response.wsgi_request.user.is_authenticated)
