from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class LikeList(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        ]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
