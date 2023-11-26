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
    