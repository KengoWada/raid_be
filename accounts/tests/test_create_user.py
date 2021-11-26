from base_test.base_test import BaseTestCase


class RegisterUserTestCase(BaseTestCase):

    def test_registering_user(self):
        """Test registering a user"""
        url = '/auth/register/'

        response = self.client.post(url, data=self.user_data, format='json')

        self.assertEqual(response.status_code, 201)

    def test_registering_user_invalid_request(self):
        """Test registering a user with invalid data"""
        url = '/auth/register/'

        response = self.client.post(
            url, data=self.invalid_user_data, format='json')

        self.assertEqual(response.status_code, 400)
