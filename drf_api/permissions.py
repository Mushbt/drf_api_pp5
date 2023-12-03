# Imports

# 3rd party
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Class for custom permissions to ensure
    users can only update or delete their content
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
