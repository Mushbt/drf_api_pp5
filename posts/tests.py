# Imports

# 3rd party
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Post


class PostListViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(username='samuel', password='password')
    
    def test_logged_out_user_can_not_create_post(self):
        """ 
        Test to ensure logged out users can't create posts
        """
        response = self.client.post('/posts/', {'country': 'Lebanon'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_logged_in_user_can_create_post(self):
        """
        Test to ensure logged in users can create posts
        """
        self.client.login(username='samuel', password='password')
        response = self.client.post('/posts/', {'title': 'post title',
        'country': 'Lebanon'})

    def test_post_must_include_all_fields(self):
        """
        Test to ensure all fields are filled before uploading post
        """
        self.client.login(username='samuel', password='password')
        response = self.client.post('/posts/', {'country': 'Lebanon'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_user_can_view_posts(self):
        """
        Test to ensure users can view posts
        """
        samuel = User.objects.get(username='samuel')
        Post.objects.create(owner=samuel, title='post title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PostDetailViewTest(APITestCase):
    """
    Contains 2 users and a post for each user
    """
    def setUp(self):
        samuel = User.objects.create_user(username='samuel', password='password')
        angelo = User.objects.create_user(username='angelo', password='password')
        Post.objects.create(
            owner=samuel, title='post title',
            description='view', country='Sweden'
        )
        Post.objects.create(
            owner=angelo, title='post title2',
            description='view2', country='Ireland'
        )

    def test_can_retrieve_existing_posts(self):
        """
        Test to ensure existing posts can be retrieved
        """
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'post title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_can_not_retrieve_non_existing_posts(self):
        """
        Test to ensure non existing posts can't be retrieved
        """
        response = self.client.get('/posts/300/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_user_can_delete_their_own_post(self):
        """
        Test to ensure user can delete their own posts
        """
        self.client.login(username='samuel', password='password')
        response = self.client.delete('/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_user_can_not_delete_other_users_post(self):
        """
        Test to ensure users can't delete other users posts
        """
        self.client.login(username='samuel', password='password')
        response = self.client.delete('/posts/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

