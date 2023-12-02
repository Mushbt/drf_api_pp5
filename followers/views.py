# Imports

# 3rd party
from rest_framework import generics, permissions

# Internal
from .models import Follower
from .serializers import FollowerSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class FollowerList(generics.ListCreateAPIView):
    """ 
    Class for FollowerList
    """
    serializer_class = FollowerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Class for FollowerDetail to allow user to
    retrieve followers and unfollow other users
    """
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()