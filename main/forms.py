from django.forms import ModelForm
from main.models import Book
from django.utils.html import strip_tags


class BookEntryForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", "author", "price", "image"]

        def clean_name(self):
            name = self.cleaned_data["name"]
            return strip_tags(name)

        def clean_author(self):
            author = self.cleaned_data["author"]
            return strip_tags(author)