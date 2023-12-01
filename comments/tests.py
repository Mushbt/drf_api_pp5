from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Comment
from posts.models import Post

class CommentListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='samuel', password='password')
    
    def test_not_logged_in_user_cannot_create_comment(self):
        response = self.client.post('/comments/', {'content': 'Amazing view!'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)