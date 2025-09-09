from api.models import Tag, Post, PostUserLikes, User, UserProfile, Comment
from api.permissions import CommentOwnerOrReadOnly, IsAdmin, PostUserLikesPermission, PostsPermission, TagsPermission, UserProfilePermission
from api.serializers import TagSerializer, CommentSerializer, PostUserLikesSerializer, PostSerializer, UserProfileSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from rest_framework.authtoken.serializers import AuthTokenSerializer
from api.auth import get_jwt

from rest_framework.response import Response
from rest_framework import status


class AuthViewSet(ViewSet):
    queryset = User.objects.all()
    serializer_class = AuthTokenSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        return Response({
            "login": 'http://localhost:8000/api/auth/login/',
            "register": 'http://localhost:8000/api/auth/register/'
        })

    @action(detail=False, methods=['post', 'get'])
    def login(self, request):
        serializer = AuthTokenSerializer(
            data=request.data, context={'request': request}
        )

        serializer.is_valid(raise_exception=True)  # 401

        user = serializer.validated_data['user']
        jwt = get_jwt(user)
        return Response(jwt)

    @action(detail=False, methods=['post', 'get'])
    def register(self, request):
        serializer = UserSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)  # 401
        # saves the user and returns the user instance
        user = serializer.save()

        jwt = get_jwt(user)

        return Response(
            {
                "message": "User registered successfully",
                **jwt,
                "user": serializer.data
            }, status=status.HTTP_201_CREATED
        )

from api.throttles import MyRateThrottle
class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [TagsPermission]
    throttle_classes = [MyRateThrottle]



from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostsPermission]
    
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['title', 'text', 'author_id']

    search_fields = ['title', 'text']
    ordering_fields = ['title', 'created_at']



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
