from django import forms

from .models import Book

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("deleted",)


class BookQueryForm(forms.Form):
    bookname = forms.CharField(required=False)
    isbn = forms.CharField(required=False)
    author = forms.CharField(required=False)
    publisher = forms.CharField(required=False)