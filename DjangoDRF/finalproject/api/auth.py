from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class BlogTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['isadmin'] = user.is_superuser
        return token


def get_jwt(user):
    token = BlogTokenObtainPairSerializer.get_token(user)
    return {'jwt': str(token.access_token)}
