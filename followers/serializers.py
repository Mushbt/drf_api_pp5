# Imports

# 3rd party
from django.db import IntegrityError
from rest_framework import serializers

# Internal
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Class for FollowSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_user = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id',
            'owner',
            'followed',
            'created_on',
            'followed_user',
        ]

    def create(self, validated_data):
        """
        For handling possible duplications
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication'
            })
