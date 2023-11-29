from rest_framework import serializers
from .models import Post
from likes.models import Like

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    comments_number = serializers.ReadOnlyField()
    likes_number = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Your image exceeds the height limit of 4096px.'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Your image exceeds the width limit of 4096px.'
            )
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Your image is too large. Max size is 2MB.'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_like_id(self,obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_on',
            'updated_on',
            'title',
            'description',
            'country',
            'image',
            'like_id',
            'comments_number',
            'likes_number',
        ]