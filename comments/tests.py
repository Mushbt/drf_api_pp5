# Imports

# 3rd party
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Comment
from posts.models import Post

class CommentListViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(username='samuel', password='password')
    
    def test_not_logged_in_user_cannot_create_comment(self):
        """
        Test to ensure users can't create comments if not logged in
        """
        response = self.client.post('/comments/', {'content': 'Amazing view!'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentDetailViewTests(APITestCase):
    def setUp(self):
        """
        Two users with post and comment for each user
        """
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
    
    def test_logged_in_user_can_create_comment(self):
        """
        Test to ensure logged in users can create comments
        """
        self.client.login(username='samuel', password='password')
        response = self.client.post('/comments/', {'post': 1, 'content': 'new comment'})
        comment_count = Comment.objects.count()
        self.assertEqual(comment_count, 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_can_retrieve_existing_comment(self):
        """
        Test to ensure users can retrieve existing comments
        """
        self.client.login(username='samuel', password='password')
        response = self.client.get('/comments/1/')
        self.assertEqual(response.data['content'], 'wow')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_can_not_retrieve_non_existing_comment(self):
        """
        Test to ensure non existing comments can't be retrieved
        """
        self.client.login(username='samuel', password='password')
        response = self.client.get('/comments/300/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_user_can_update_their_own_comment(self):
        """
        Test to ensure users can update their own comments
        """
        self.client.login(username='samuel', password='password')
        response = self.client.put('/comments/1/', {'content': 'updated comment'})
        comment = Comment.objects.filter(pk=1).first()
        self.assertEqual(comment.content, 'updated comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_can_not_update_other_users_comment(self):
        """
        Test to ensure user can't update other user's comments
        """
        self.client.login(username='samuel', password='password')
        response = self.client.put('/comments/2/', {'content': 'updated comment'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_user_can_delete_their_own_comment(self):
        """
        Test to ensure user can delete their own comments
        """
        self.client.login(username='samuel', password='password')
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_user_can_not_delete_other_users_comment(self):
        """
        Test to ensure users can't delete other users comments
        """
        self.client.login(username='samuel', password='password')
        response = self.client.delete('/comments/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    
   