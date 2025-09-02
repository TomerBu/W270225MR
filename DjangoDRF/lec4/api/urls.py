from api.views import index
from django.urls import path

urlpatterns = [
    path('students/', index, name='index')
]
