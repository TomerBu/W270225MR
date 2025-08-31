from django.urls import path
from quotes.views import add_quote, get_quotes, delete_quote, edit_quote

urlpatterns = [
    # /quotes/
    path('', get_quotes, name='quotes'),

    # /quotes/add
    path('add', add_quote, name='add_quote'),

    # /quotes/delete/2
    path('delete/<int:id>', delete_quote, name='delete_quote'),

    # /quotes/edit/3
    path('edit/<int:id>', edit_quote, name='edit_quote'),
]