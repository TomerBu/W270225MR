from api.models import UserProfile, Tag
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