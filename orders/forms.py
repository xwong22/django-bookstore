from django import forms

from .models import Order

from books.models import Book
# from users.models import User

class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "quantity"
        ]


class OrderCompleteForm(forms.Form):
    completed = forms.BooleanField()

    # def clean(self):
    #     cleaned_data = super().clean()
    #     return cleaned_data


class OrderQueryForm(forms.Form):
    # user = forms.ModelChoiceField(queryset=User.objects.all(), label="User", required=False)
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label="Book", required=False)
    completed = forms.BooleanField(required=False)