from django.urls import path
from students.views import all, me

urlpatterns = [
    path('all/', all, name='all'),
    path('me/', me, name='me'),
]
