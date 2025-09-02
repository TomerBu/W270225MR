from rest_framework import serializers
from api.models import Student
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

    # https://www.django-rest-framework.org/api-guide/serializers/
    # POST
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # PUT
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
