from django.shortcuts import render, redirect
from quotes.models import Quote
from django.http import HttpRequest


def get_quotes(req):
    # get all quotes from db
    quotes = Quote.objects.all().order_by('-year')
    return render(req, 'quotes/list.html', {'quotes': quotes})


def delete_quote(req: HttpRequest, id):

    try:
        quote = Quote.objects.get(id=id)
        quote.delete()
        return redirect('/quotes/')
    except Quote.DoesNotExist:
        return render(req, 'quotes/404.html', status=404)


def edit_quote(req: HttpRequest, id):
    try:
        quote = Quote.objects.get(id=id)

        if req.method == "GET":
            return render(req, "quotes/edit.html", {"quote": quote})

        quote.author = req.POST.get('author', quote.author)
        quote.quote = req.POST.get('quote', quote.quote)
        quote.year = req.POST.get('year', quote.year)
        quote.save()
        return redirect('/quotes/')
    except Quote.DoesNotExist:
        return render(req, 'quotes/404.html', status=404)


def add_quote(req: HttpRequest):
    if req.method == "GET":
        return render(req, "quotes/add.html")

    # ניקח את המידע מהטופס - וניצור קווט חדש ונשמור!
    author = req.POST.get('author')
    quote = req.POST.get('quote')
    year = req.POST.get('year')

    q = Quote(quote=quote, author=author, year=year)
    q.save()

    return redirect('/quotes/')
