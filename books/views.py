from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Book
from .form import BookForm

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/booklist.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/bookdetail.html'


class BookCreateView(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/bookcreate.html'


class BookEditView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price']
    template_name = 'books/book_edit.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/bookdelete.html'
    success_url = reverse_lazy('book_list')
