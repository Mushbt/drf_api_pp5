# Imports

# 3rd party
from rest_framework import generics, permissions

# Internal
from .models import Like
from .serializers import LikeSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class LikeList(generics.ListCreateAPIView):
    """
    Class for LikeList
    """
    serializer_class = LikeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        ]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Class for LikeDetail which allows user to retrieve and delete
    their likes
    """
    serializer_class =  LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()