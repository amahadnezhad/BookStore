from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404 , render

from .models import Book
from .forms import BookForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = "books/book_list.html"


def book_detail_view(request, pk):
    # Get Book Object
    book = get_object_or_404(Book, pk=pk)
    # Get Book Comments
    book_comments = book.comments.all()
    return render(request, 'books/book_detail.html', {'book': book, 'comments': book_comments})


class BookCreateView(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = "books/book_update.html"


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
