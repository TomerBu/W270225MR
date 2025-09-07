from api.models import Post, UserProfile, Tag, PostUserLikes, Comment
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

# json + create/update + validations


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        # fields = ['bio', 'id']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostUserLikesSerializer(ModelSerializer):
    class Meta:
        model = PostUserLikes
        fields = '__all__'

from rest_framework import serializers
from django.core.validators import RegexValidator

class UserSerializer(ModelSerializer):
    password = serializers.CharField(
        validators = [
            RegexValidator(
                regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$',
                message="Password must be at least 8 characters long and contain at least one letter and one number."
            )
        ]
    )
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
