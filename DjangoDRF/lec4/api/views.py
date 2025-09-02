from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Student
from api.serializers import StudentSerializer


@api_view(['GET', 'POST'])
def index(request: Request):
    if request.method == 'POST':
        # request.data (body)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # will invoke create
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # GET
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response({'students': serializer.data})


@api_view(['GET', 'PUT', 'DELETE'])
def details(request: Request, id: int):

    if request.method == "GET":
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == "DELETE":
        student = Student.objects.get(id=id)
        student.delete()
        return Response({'message': 'deleted'}, status=status.HTTP_200_OK)

    if request.method == "PUT":
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
