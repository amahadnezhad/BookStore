from django import forms

from .models import Book, Comment


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'price', 'cover', ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
