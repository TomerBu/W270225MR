from django.shortcuts import render
from django.http import HttpResponse

def get_quotes(request):
    return HttpResponse('Mike')
