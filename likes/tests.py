from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Like
from posts.models import Post

class LikeListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='samuel', password='password')
    
    def test_not_logged_in_user_can_not_like_post(self):
        response = self.client.post('/likes/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)