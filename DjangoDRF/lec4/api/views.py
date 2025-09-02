from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Student
from api.serializers import StudentSerializer


@api_view(['GET'])
def index(request: Request):
    students = Student.objects.all()

    # serializer = convert objects to JSON
    serializer = StudentSerializer(students, many=True)

    return Response({'students': serializer.data})
