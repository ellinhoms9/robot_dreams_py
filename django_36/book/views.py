from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from book.models import Books


def all_books(request):
    books = Books.objects.all()
    data = [{'id': books.id, 'title': books.title, 'author': books.author,
             'year': books.year, 'price': books.price}for books in books]
    return JsonResponse(data, safe=False)
