from django.urls import path
from students.views import all, me, get_names, add_name
from students.views import add_html, edit_html, list_html

urlpatterns = [
    path('add/', add_html, name='add'),
    path('edit/', edit_html, name='edit'),
    path('list/', list_html, name='list'),
    path('all/', all, name='all'),
    path('me/', me, name='me'),
    path('names/', get_names, name='getnames'),
    path('add_name/', add_name, name='add_name'),
]
