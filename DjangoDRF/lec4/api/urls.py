from api.views import index, details
from django.urls import path

urlpatterns = [
    path('students/', index, name='index'),
    path('students/<int:id>/', details, name='student_detail'),
]


# API Endpoints
# REST API:
# List all students
# GET /api/students/

# Student Detail (by id)
# GET /api/students/1
# DELETE /api/students/1
# PUT /api/students/1