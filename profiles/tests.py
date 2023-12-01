from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Profile

class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='samuel', password='password')
        User.objects.create_user(username='angelo', password='password')
    
    def test_user_can_view_existing_profile(self):
        self.client.login(username='samuel', password='password')
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_can_not_view_non_existing_profile(self):
        self.client.login(username='samuel', password='password')
        response = self.client.get('/profiles/300/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_user_can_update_their_own_profile(self):
        self.client.login(username='samuel', password='password')
        response = self.client.put('/profiles/1/',
        {'content': 'hello lebanon!'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.content, 'hello lebanon!')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
