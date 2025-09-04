from api.views import say_hello, Students, StudentsById
from django.urls import path

urlpatterns = [
    path('hello/', say_hello),
    path('students/', Students.as_view(), name='students'),
    path('students/<int:pk>/', StudentsById.as_view(), name='student_detail'),
]