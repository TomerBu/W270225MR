from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def foo(request):
    return HttpResponse('foo')

def bar(request):
    return HttpResponse('bar')

def hi(request):
    return HttpResponse('Hola')
