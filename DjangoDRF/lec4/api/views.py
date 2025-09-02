from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Student, Kitten
from api.serializers import StudentSerializer, KittenSerializer


from rest_framework.views import APIView


class KittensView(APIView):
    def get(self, request):
        kittens = Kitten.objects.all()
        serializer = KittenSerializer(kittens, many=True)
        return Response({"kittens": serializer.data})

    def post(self, request: Request):
        kitten = KittenSerializer(data=request.data)
        if kitten.is_valid():
            kitten.save()
            return Response(kitten.data, status=status.HTTP_201_CREATED)
        return Response({"errors": kitten.errors}, status=status.HTTP_400_BAD_REQUEST)


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
