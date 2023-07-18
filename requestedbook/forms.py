from django import forms
from .models import Requestedbook

class RequestedbookModelForm(forms.ModelForm):
    class Meta:
        model = Requestedbook
        fields = [
        'RBName',
        'RBAuthor',
        'Quantity',
        ]
