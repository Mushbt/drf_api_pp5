from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class CommentList(APIView):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        posts = Comment.objects.all()
        serializer = CommentSerializer(
            posts,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)