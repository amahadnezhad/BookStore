from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render

from .models import Book
from .form import BookForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/booklist.html'
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/bookdetail.html'

def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()

    return render(request, 'books/bookdetail.html', context={'book': book, 'comments': comments})


class BookCreateView(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/bookcreate.html'


class BookEditView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover',]
    template_name = 'books/book_edit.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/bookdelete.html'
    success_url = reverse_lazy('book_list')
