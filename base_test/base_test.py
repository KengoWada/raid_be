from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

User = get_user_model()


class BaseTestCase(APITestCase):

    def setUp(self):
        # Dummy users
        self.user_data = {
            'email': 'test.user@email.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'Compl3xpassword'
        }
        self.other_user_data = {
            'email': 'other.user@email.com',
            'first_name': 'Other',
            'last_name': 'User',
            'password': 'Compl3xpassword'
        }
        self.invalid_user_data = {
            'email': 'other.user@ema',
            'first_name': 'Other',
            'last_name': 'User',
            'password': 'Compl3xpassword'
        }
        self.update_user_data = {
            'first_name': 'Updated',
            'last_name': 'Name'
        }
        self.invalid_update_user_data = {
            'last_name': 'Name'
        }

    def create_user(self, data):
        user_data = data.copy()

        email = user_data.pop('email')
        password = user_data.pop('password')

        return User.objects.create_user(email, password, **user_data)
