from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy

from book.models import Books
from django.views.generic import ListView, DetailView, CreateView


class BookListView(ListView):
    model = Books


class BookDetailView(DetailView):
    model = Books


class BooksCreateView(CreateView):
    model = Books
    template_name = 'book/books_create.html'
    context_object_name = 'books/books_create.html'
    fields = ('title', 'author', 'year', 'price')
    success_url = reverse_lazy('books:books-list')
