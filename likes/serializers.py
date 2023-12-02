# Imports

# 3rd party
from django.db import IntegrityError
from rest_framework import serializers

#Internal
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Class for LikeSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id',
            'owner',
            'created_on',
            'post',
        ]
    
    def create(self, validated_data):
        """
        Handles possible duplications from same users
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication'
            })