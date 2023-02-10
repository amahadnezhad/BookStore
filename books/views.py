from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render

from .models import Book
from .forms import BookForm , CommentForm


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
    comments = book.comments.filter(is_active=True)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'books/bookdetail.html', context={'book': book,
                                                             'comments': comments,
                                                             'comment_form': comment_form,
                                                             })


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
