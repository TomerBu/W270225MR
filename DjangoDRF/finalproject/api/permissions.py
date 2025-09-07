from rest_framework import permissions


class CommentOwnerOrReadOnly(permissions.BasePermission):

    # /api/comments
    def has_permission(self, request, view):
         if request.method in permissions.SAFE_METHODS:
            return True
         return request.user and request.user.is_authenticated

    # /api/comments/{id}
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if hasattr(obj, 'author') and hasattr(obj.author, 'user'):
            return obj.author.user == request.user

        return False


class PostsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff and request.user.is_superuser


class TagsPermission(PostsPermission):
    """
      Inherits from PostsPermission to apply the same rules for Tags.
    """


class UserProfilePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj.user.user


class PostUserLikesPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj.user


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
