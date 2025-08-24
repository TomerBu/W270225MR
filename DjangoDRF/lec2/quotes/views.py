from django.shortcuts import render
from django.http import HttpResponse

from quotes.models import Quote
 

def get_quotes(req):
    quotes = Quote.objects.all()
    return render(req, 'quotes/list.html' , {'quotes': quotes})
