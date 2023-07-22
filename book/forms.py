from django import forms
from book.models import BookstoreModel

class BookStorForm(forms.ModelForm):
    class Meta:
        model = BookstoreModel
        exclude = ['first_pub','last_pub']