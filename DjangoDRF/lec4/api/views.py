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
    
    return Response("TODO: complete this")
