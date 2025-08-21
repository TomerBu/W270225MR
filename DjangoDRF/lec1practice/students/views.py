from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
names = ['Dani', 'Alice', 'Bob']


def all(request):
    return HttpResponse("all")


def me(request):
    return HttpResponse("me")


def get_names(request):
    # return 'Dani Alice Bob'
    return HttpResponse(" ".join(names))


@csrf_exempt  #temp disable CSRF verification
def add_name(request:HttpRequest):
    if request.method == 'POST':
        return HttpResponse("POST")
    else:
        return HttpResponse("Not POST", status=403)


# http://127.0.0.1:8000/students/add_name/