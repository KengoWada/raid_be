from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.test import APITestCase

from uploads.serializers import XrayUploadSerializer

User = get_user_model()


class BaseTestCase(APITestCase):

    def setUp(self):
        # Dummy users
        self.user_data = {
            'email': 'test.user@email.com',
            'first_name': 'Test',
            'last_name': 'User',
            'avatar': 'https://somelink.com/img.png',
            'password': 'Compl3xpassword'
        }
        self.other_user_data = {
            'email': 'other.user@email.com',
            'first_name': 'Other',
            'last_name': 'User',
            'avatar': 'https://somelink.com/img2.png',
            'password': 'Compl3xpassword'
        }
        self.invalid_user_data = {
            'email': 'other.user@email.com',
            'first_name': 'Other',
            'last_name': 'User',
            'password': 'Compl3xpassword'
        }
        self.update_user_data = {
            'first_name': 'Updated',
            'last_name': 'Name',
            'avatar': 'https://somelink.com/img3.png',
        }
        self.invalid_update_user_data = {
            'last_name': 'Name'
        }

        self.xray_upload = {
            'uuid': '2456d79b-2c13-4012-af13-a5f300350689',
            'description': 'Patient ID: 123456, Case Number: 123456',
            'images': ['https://somelink.com/img1.png', 'https://somelink.com/img1.png']
        }
        self.other_xray_upload = {
            'uuid': 'bec3cf7e-4dd8-415d-9fbf-758760c1f1f3',
            'description': 'Patient ID: 654321, Case Number: 654321',
            'images': ['https://somelink.com/img1.png', 'https://somelink.com/img1.png']
        }
        self.invalid_xray_upload = {
            'uuid': '8ff77f9a-7600-4f7f-8b76-48bc5b214712',
            'description': 'Patient ID: 123456, Case Number: 123456',
            'images': []
        }
        self.update_xray_upload = {
            'description': 'Patient ID: 654, Case Number: 321'
        }

    def create_user(self, data):
        user_data = data.copy()

        email = user_data.pop('email')
        password = user_data.pop('password')

        return User.objects.create_user(email, password, **user_data)

    def create_xray_upload(self, data, user_data):
        user = self.create_user(user_data)
        upload_data = data.copy()

        serializer = XrayUploadSerializer(data=upload_data)
        if not serializer.is_valid():
            return None

        serializer.save(user=user)
        return {'upload': serializer.instance, 'user': user}
