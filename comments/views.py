# Imports

# 3rd party
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

# Internal
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class CommentList(generics.ListCreateAPIView):
    """
    Class for CommentList to view comments
    """
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        ]
    queryset = Comment.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'post', # Get all comments for a specific post
        'owner', # Get all comments for a specific user
    ]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Class for CommentDetail to retrieve, edit and delete their comments
    """
    serializer_class = CommentDetailSerializer
    permission_classes = [
        IsOwnerOrReadOnly
        ]
    queryset = Comment.objects.all()
