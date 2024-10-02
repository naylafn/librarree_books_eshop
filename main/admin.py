from django.contrib import admin

# Register your models here.
from .models import Book  # Replace with your model name

admin.site.register(Book)  # Register your model