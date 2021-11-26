from base_test.base_test import BaseTestCase


class UpdateUserTestCase(BaseTestCase):

    def test_update_user(self):
        """Test update user details"""
        user = self.create_user(self.user_data)

        url = '/auth/user/'

        self.client.force_authenticate(user=user)
        response = self.client.put(
            url, data=self.update_user_data, format='json')

        self.assertEqual(response.status_code, 200)

    def test_update_user_not_authenticated(self):
        """Test updating a users details"""
        self.create_user(self.user_data)

        url = '/auth/user/'

        response = self.client.put(
            url, data=self.update_user_data, format='json')

        self.assertEqual(response.status_code, 401)

    def test_update_user_invalid_details(self):
        """Test updating a user with invalid data"""
        user = self.create_user(self.user_data)

        url = '/auth/user/'

        self.client.force_authenticate(user=user)
        response = self.client.put(
            url, data=self.invalid_update_user_data, format='json')

        self.assertEqual(response.status_code, 400)
