from django.urls import path
from students.views import all, me, get_names, add_name

urlpatterns = [
    path('all/', all, name='all'),
    path('me/', me, name='me'),
    path('names/', get_names, name='getnames'),
    path('add_name/', add_name, name='add_name'),
]
