from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import api_view


class StudentsViewSet(ViewSet):
    def list(self, request: Request) -> Response:
        return Response({"message": "GET"})

    def create(self, request: Request) -> Response:
        return Response({"message": "POST"})
    
    def retrieve(self, request: Request, pk: int) -> Response:
        return Response({"message": "GET"})

    def update(self, request: Request, pk: int) -> Response:
        return Response({"message": "PUT"})

    def partial_update(self, request: Request, pk: int) -> Response:
        return Response({"message": "PATCH"})   

    def destroy(self, request: Request, pk: int) -> Response:
        return Response({"message": "DELETE"})

# function based views
@api_view(['GET'])
def say_hello(request: Request) -> Response:
    return Response({"message": "Hello, world!"})



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