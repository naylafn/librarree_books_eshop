from django.forms import ModelForm
from main.models import Book

class BookEntryForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", "author", "price", "image"]