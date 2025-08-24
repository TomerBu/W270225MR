from django.shortcuts import render
from django.http import HttpResponse


quotes = ["Life is what happens when you're busy making other plans.",
          "The greatest glory in living lies not in never falling, but in rising every time we fall.",
          "In the end, we will remember not the words of our enemies, but the silence of our friends.˝"]


def get_quotes(req):
    return HttpResponse("<hr>".join(quotes))


def get_single_quote(req, id):
    return HttpResponse(quotes[id])