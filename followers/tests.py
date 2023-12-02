# Imports

# 3rd party
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Follower


class FollowerListViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(username='samuel', password='password')
    
    def test_not_logged_in_user_can_not_follow(self):
        """
        Test to ensure users who are not logged in not being able to follow other users
        """
        response = self.client.post('/followers/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FollowerDetailViewTests(APITestCase):
    """ 
    Class for FollowerDetailView which contains
    3 users and 3 follows
    """
    def setUp(self):
        samuel = User.objects.create_user(username='samuel', password='password')
        angelo = User.objects.create_user(username='angelo', password='password')
        ayla = User.objects.create_user(username='ayla', password='password')

        Follower.objects.create(owner=samuel, followed_id=2)
        Follower.objects.create(owner=angelo, followed_id=3)
        Follower.objects.create(owner=ayla, followed_id=1)
    
    def test_logged_in_user_can_follow_others(self):
        """
        Test to ensure logged in user can follow other users
        """
        self.client.login(username='samuel', password='password')
        response = self.client.post('/followers/', {'followed': 3})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_retrieve_existing_following(self):
        """
        Test to ensure user can retrieve existing following using valid ID
        """
        self.client.login(username='samuel', password='password')
        response = self.client.get('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_can_not_retrieve_non_existing_following(self):
        """
        Test to ensure user can not retrieve a following from a non valid ID
        """
        self.client.login(username='samuel', password='password')
        response = self.client.get('/followers/300/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_user_can_unfollow(self):
        """
        Test to ensure user can unfollow other users
        """
        self.client.login(username='samuel', password='password')
        response = self.client.delete('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_unfollow_other_users_followers(self):
        """
        Test to ensure user can not remove other users followers
        """
        self.client.login(username='samuel', password='password')
        response = self.client.delete('/followers/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
