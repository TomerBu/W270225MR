from django.contrib import admin
from django.urls import path, include
from quotes.urls import urlpatterns as quote_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quotes/', include(quote_patterns))
]