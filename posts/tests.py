from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='samuel', password='password')
    
    def test_logged_out_user_can_not_create_post(self):
        response = self.client.post('/posts/', {'country': 'Lebanon'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_logged_in_user_can_create_post(self):
        self.client.login(username='samuel', password='password')
        response = self.client.post('/posts/', {'title': 'post title',
        'country': 'Lebanon'})

    def test_post_must_include_all_fields(self):
        self.client.login(username='samuel', password='password')
        response = self.client.post('/posts/', {'country': 'Lebanon'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_user_can_view_posts(self):
        samuel = User.objects.get(username='samuel')
        Post.objects.create(owner=samuel, title='post title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PostDetailViewTest(APITestCase):
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
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'post title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_can_not_retrieve_non_existing_posts(self):
        response = self.client.get('/posts/300/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_user_can_delete_their_own_post(self):
        self.client.login(username='samuel', password='password')
        response = self.client.delete('/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_user_can_not_delete_other_users_post(self):
        self.client.login(username='samuel', password='password')
        response = self.client.delete('/posts/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

