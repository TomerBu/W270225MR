from rest_framework import serializers
from api.models import Kitten, Student
from django.core.validators import MinValueValidator, MaxValueValidator

class KittenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitten
        fields = ['id', 'name', 'breed']
        # fields = '__all__'
        # exclude = ['id']


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(
        validators=[MinValueValidator(4), MaxValueValidator(120)]
    )

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance


# https://www.django-rest-framework.org/api-guide/serializers/
