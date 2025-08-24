from django.urls import path
from quotes.views import add_quote, get_quotes

urlpatterns = [
    path('', get_quotes, name='quotes'),
    path('add', add_quote, name='add_quote')
]