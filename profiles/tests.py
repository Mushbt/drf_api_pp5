# Imports

# 3rd party
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Profile


class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        """
        Creates two user instances
        """
        User.objects.create_user(username='samuel', password='password')
        User.objects.create_user(username='angelo', password='password')
    
    def test_user_can_view_existing_profile(self):
        """
        Test to ensure user can view other user profiles
        """
        self.client.login(username='samuel', password='password')
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_can_not_view_non_existing_profile(self):
        """
        Test to ensure user can not view non existing profiles
        """
        self.client.login(username='samuel', password='password')
        response = self.client.get('/profiles/300/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_user_can_update_their_own_profile(self):
        """
         Test to ensure user can update their own profile
         """
        self.client.login(username='samuel', password='password')
        response = self.client.put('/profiles/1/',
        {'description': 'hello lebanon!'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.description, 'hello lebanon!')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_can_not_update_other_profiles(self):
        """
        Test to ensure user can't update other users profiles
        """
        self.client.login(username='samuel', password='password')
        response = self.client.put('/profiles/2/', {'description': 'hello brazil!'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_not_logged_in_user_can_not_update_their_own_profile(self):
        """
        Test to ensure users can't update their profiles if not logged in
        """
        response = self.client.put('/profiles/1/',
        {'description': 'hello germany'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_user_can_delete_their_profile(self):
        """
        Test to ensure user can delete their own profile
        """
        self.client.login(username='samuel', password='password')
        response = self.client.delete('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
