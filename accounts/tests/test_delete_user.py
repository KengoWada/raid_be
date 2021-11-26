from base_test.base_test import BaseTestCase


class DeleteUserTestCase(BaseTestCase):

    def test_delete_user(self):
        """Test deleting a user"""
        user = self.create_user(self.user_data)

        url = '/auth/user/'

        self.client.force_authenticate(user=user)
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, 200)

    def test_delete_user_not_authenticated(self):
        """Test deleting a user when not logged in"""
        self.create_user(self.user_data)

        url = '/auth/user/'

        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, 401)
