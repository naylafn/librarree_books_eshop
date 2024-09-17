from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import BookEntryForm
from main.models import Book
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    book_entries = Book.objects.all()
    context = {
        'application' : 'Librarree',
        'name': 'Nayla Farah Nida',
        'class': 'PBP F',
        'book_entries': book_entries,
    }
    return render(request, "main.html", context)

def create_book_entry(request):
    form = BookEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_book_entry.html", context)

def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")