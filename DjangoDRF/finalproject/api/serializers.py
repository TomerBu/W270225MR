from rest_framework import serializers
from django.core.validators import RegexValidator
from api.models import Post, UserProfile, Tag, PostUserLikes, Comment
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class CurrentProfileDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.userprofile


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
    author = serializers.HiddenField(
        default=CurrentProfileDefault()
    )
    author_id = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_author_id(self, obj):
        return obj.author.id


class CommentSerializer(ModelSerializer):
    author = serializers.HiddenField(
        default=CurrentProfileDefault()
    )
    author_id = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_author_id(self, obj):
        return obj.author.id


class PostUserLikesSerializer(ModelSerializer):
    user = serializers.HiddenField(
        default=CurrentProfileDefault()
    )
    user_id = serializers.SerializerMethodField()

    class Meta:
        model = PostUserLikes
        fields = '__all__'

    def get_user_id(self, obj):
        return obj.user.id


class UserSerializer(ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    user_id = serializers.SerializerMethodField('get_user_id')
 
    password = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$',
                message="Password must be at least 8 characters long and contain at least one letter and one number."
            )
        ],
        write_only=True
    )

    def get_user_id(self, obj):
        return obj.id

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # remove the password from the dictionary
        password = validated_data.pop('password', None)

        # iterate over the dict and set the attributes of the user instance
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'user_id', 'user']
        extra_kwargs = {'password': {'write_only': True}}
