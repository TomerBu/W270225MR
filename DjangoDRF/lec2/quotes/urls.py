from django.urls import path
from quotes.views import get_quotes

urlpatterns = [
    path('', get_quotes),
]