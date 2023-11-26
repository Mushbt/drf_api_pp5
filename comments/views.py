from rest_framework import generics, permissions
from .serializers import CommentSerializer, CommentDetailSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        ]
    queryset = Comment.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentDetailSerializer
    permission_classes = [
        IsOwnerOrReadOnly
        ]
    queryset = Comment.objects.all()
