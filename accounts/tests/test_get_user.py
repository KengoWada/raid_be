from base_test.base_test import BaseTestCase


class GetUserTestCase(BaseTestCase):

    def test_get_user_details(self):
        """Test getting a users details"""
        user = self.create_user(self.user_data)

        url = '/auth/user/'

        self.client.force_authenticate(user=user)
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)

    def test_get_user_details_not_authenticated(self):
        """Test getting a users details when not authenticated"""
        self.create_user(self.user_data)

        url = '/auth/user/'

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 401)
