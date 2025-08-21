from django.contrib import admin
from django.urls import path, include
from students.urls import urlpatterns as students_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include(students_urls)),
]
