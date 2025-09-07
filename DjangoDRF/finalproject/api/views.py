from api.models import Tag, Post, PostUserLikes, User, UserProfile, Comment
from api.permissions import CommentOwnerOrReadOnly, IsAdmin, PostUserLikesPermission, PostsPermission, TagsPermission, UserProfilePermission
from api.serializers import TagSerializer, CommentSerializer, PostUserLikesSerializer, PostSerializer, UserProfileSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [TagsPermission]


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostsPermission]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentOwnerOrReadOnly]


class PostUserLikesViewSet(ModelViewSet):
    queryset = PostUserLikes.objects.all()
    serializer_class = PostUserLikesSerializer
    permission_classes = [PostUserLikesPermission]


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [UserProfilePermission]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
