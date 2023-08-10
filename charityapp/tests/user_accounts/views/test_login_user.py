from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class CustomLoginViewTests(TestCase):
    def test_login_view_template(self):
        response = self.client.get(reverse('login-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_accounts/login-page.html')

    def test_login_valid_user(self):
        user_data = {
            'email': 'l@abv.bg',
            'password': 'l12345@!',
            'user_type': 'MEMBER',
        }

        UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)

        response = self.client.post(reverse('login-page'), **user_data)

        self.assertEqual(response.status_code, 302)

