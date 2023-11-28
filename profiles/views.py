from django.db.models import Count
from rest_framework import generics, status, filters
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_number=Count(
            'owner__post',
            distinct=True
        ),
        followers_number=Count(
            'owner__followed',
            distinct=True
        ),
        following_number=Count(
            'owner__following',
            distinct=True
        )
    ).order_by('-created_on')


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    
    def delete(self, request, pk):
        user = self.request.user
        user.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )