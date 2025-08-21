from django.http import HttpResponse

def all(request):
    return HttpResponse("all")

def me(request):
    return HttpResponse("me")