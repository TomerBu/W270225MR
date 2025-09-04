from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request


from rest_framework.decorators import api_view
# Create your views here.

# function based views
@api_view(['GET'])
def say_hello(request: Request) -> Response:
    return Response({"message": "Hello, world!"})


from rest_framework.views import APIView
class Students(APIView):
    def get(self, request: Request) -> Response:
        return Response({"message": "GET"})

    def post(self, request: Request) -> Response:
        return Response({"message": "POST"})
    

class StudentsById(APIView):
    def get(self, request: Request, pk: int) -> Response:
        return Response({"message": "GET"})

    def post(self, request: Request, pk: int) -> Response:
        return Response({"message": "POST"})

    def delete(self, request: Request, pk: int) -> Response:
        return Response({"message": "DELETE"})

    def put(self, request: Request, pk: int) -> Response:
        return Response({"message": "PUT"})