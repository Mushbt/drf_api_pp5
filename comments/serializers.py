# Imports

# 3rd party
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

# Internal
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Class for the CommentSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    # How long ago comment was created
    def get_created_on(self,obj):
            return naturaltime(obj.created_on)
    # How long ago comment was updated    
    def get_updated_on(self, obj):
            return naturaltime(obj.updated_on)

    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'post',
            'created_on',
            'updated_on',
            'content',
            'profile_id',
            'profile_image',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Class for CommentDetail which inherits from CommentSerializer
    """
    post = serializers.ReadOnlyField(source='post.id')