from api.views import TagViewSet, PostViewSet, CommentViewSet, PostUserLikesViewSet, UserProfileViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

from django.urls import path, include
router = DefaultRouter()
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'post-user-likes', PostUserLikesViewSet, basename='post-user-likes')
router.register(r'user-profiles', UserProfileViewSet, basename='user-profiles')
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls

# add login links to browsable api:
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]