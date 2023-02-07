from django.shortcuts import render
from django.views import generic

from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/booklist.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/bookdetail.html'

