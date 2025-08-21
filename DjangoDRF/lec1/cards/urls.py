from django.urls import path
from cards.views import hi, foo, bar

urlpatterns = [
    path("hi/", hi, name="hi"),
    path("foo/", foo, name="foo"),
    path("bar/", bar, name="bar"),
]
