# Imports

# 3rd party
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Like
from posts.models import Post

class LikeListViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(username='samuel', password='password')
    
    def test_not_logged_in_user_can_not_like_post(self):
        """
        Test to ensure users who are not logged in not able to like posts
        """
        response = self.client.post('/likes/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class LikeDetailViewTests(APITestCase):
    def setUp(self):
        """
        Contains 2 users, 2 posts and 1 like per post
        """
        samuel = User.objects.create_user(username='samuel', password='password')
        angelo = User.objects.create_user(username='angelo', password='password')
        Post.objects.create(
            owner=samuel, title='wildlife', description='spring', country='Lebanon'
        )
        Post.objects.create(
            owner=angelo, title='seaside', description='summer', country='Greece'
        )
        Like.objects.create(owner=samuel, post_id=2)
        Like.objects.create(owner=angelo, post_id=1)
    
    def test_logged_in_user_can_like_post(self):
        """
        Test to ensure logged in users can like posts
        """
        self.client.login(username='samuel', password='password')
        response = self.client.post('/likes/', {'post': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_can_retrieve_existing_like(self):
        """
        Test to ensure user can retrieve existing likes using valid ID
        """
        self.client.login(username='samuel', password='password')
        response = self.client.get('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_can_not_retrieve_non_existing_like(self):
        """
        Test to ensure user can't retrieve likes with no valid ID
        """
        self.client.login(username='samuel', password='password')
        response = self.client.get('/likes/300/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_user_can_unlike_own_like(self):
        """
        Test to ensure user can unlike a post they have liked
        """
        self.client.login(username='samuel', password='password')
        response = self.client.delete('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_user_can_unlike_other_user_like(self):
        """
        Test to ensure user can't remove other users likes
        """
        self.client.login(username='samuel', password='password')
        response = self.client.delete('/likes/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
