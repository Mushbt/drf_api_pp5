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


class CommentDetailViewTests(APITestCase):
    def setUp(self):
        samuel = User.objects.create_user(username='samuel', password='password')
        angelo = User.objects.create_user(username='angelo', password='password')
        Post.objects.create(
            owner=samuel, title='post title',
            description='scenic', country='Lebanon')
        Post.objects.create(
            owner=angelo, title='post title 2',
            description='wildlife', country='Brazil')
        Comment.objects.create(owner=samuel, post_id=1, content='wow')
        Comment.objects.create(owner=angelo, post_id=2, content='amazing')