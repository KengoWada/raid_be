from base_test.base_test import BaseTestCase


class LoginUserTestCase(BaseTestCase):

    def test_login_user(self):
        """Test login user"""
        self.create_user(self.user_data)

        url = '/auth/login/'
        data = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, 200)

    def test_login_invalid_credentials(self):
        """Test logging in with invalid credentials"""
        self.create_user(self.user_data)

        url = '/auth/login/'
        data = {'email': self.user_data['email'], 'password': 'wrong_password'}

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, 400)
