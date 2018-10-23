from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User


class SignUpTestCaste(APITestCase):
    url = '/api/users/register/'
    client = APIClient()

    def setUp(self):
        self.data = {
            'username': 'test',
            'password': '1234',
            'email': '2222@aaa.bbb'
        }
        self.client = APIClient()

    def test_signup_valid_data_should_save_object_to_db(self):
        pre_register_users_count = User.objects.count()
        response = self.client.post(self.url, data=self.data)
        post_register_users_count = User.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(pre_register_users_count+1, post_register_users_count)

    def test_password_should_not_be_in_response(self):
        response = self.client.post(self.url, data=self.data)
        self.assertTrue('password' not in response.data, 'Password is visible in response body ')

