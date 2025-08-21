from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

names = ['Dani', 'Alice', 'Bob']

def list_html(request):

    return render(request, 'students/list.html', {'names': names})

def add_html(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            names.append(name)
        return HttpResponseRedirect('/students/list')
    

    return render(request, 'students/add.html')

def edit_html(request):
    return render(request, 'students/edit.html')












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