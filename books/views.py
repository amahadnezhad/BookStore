from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404 , render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Book
from .forms import BookForm, CommentForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = "books/book_list.html"


def book_detail_view(request, pk):
    # Get Book Object
    book = get_object_or_404(Book, pk=pk)
    # Get Book Comments
    book_comments = book.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'books/book_detail.html', {'book': book,
                                                      'comments': book_comments,
                                                      'comment_form': CommentForm,
                                                      })


class BookCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_create.html'
    success_message = 'Book Has SuccessFully Created'


class BookUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = "books/book_update.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    success_message = 'Book Has SuccessFully Updated'


class BookDeleteView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    success_message = 'Book Has SuccessFully ِDeleted'
