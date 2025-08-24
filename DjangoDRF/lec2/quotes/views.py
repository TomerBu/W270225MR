from django.shortcuts import render, redirect
from quotes.models import Quote
from django.http import HttpRequest


def get_quotes(req):
    quotes = Quote.objects.all().order_by('-year')
    return render(req, 'quotes/list.html', {'quotes': quotes})


def add_quote(req: HttpRequest):
    if req.method == 'POST':
        author = req.POST.get('author')
        quote = req.POST.get('quote')
        year = req.POST.get('year')

        if author and quote and year:
            quote = Quote(author=author, quote=quote, year=year)
            quote.save()
        else:
            return render(req, 'quotes/add.html', {'error': 'must fill all the fields'})

        return redirect('quotes')

    return render(req, 'quotes/add.html')
