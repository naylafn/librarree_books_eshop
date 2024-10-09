from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import BookEntryForm
from main.models import Book
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

import datetime
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    # book_entries = Book.objects.filter(user=request.user)
    context = {
        'application' : 'Librarree',
        'name': request.user.username,
        'class': 'PBP F',
        # 'book_entries': book_entries,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def create_book_entry(request):
    form = BookEntryForm(request.POST, request.FILES)

    if form.is_valid() and request.method == "POST":
        book_entry = form.save(commit=False)
        book_entry.user = request.user
        book_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_book_entry.html", context)

def show_xml(request):
    data = Book.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_book(request, id):
    book = Book.objects.get(pk = id)
    form = BookEntryForm(request.POST or None, instance=book)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_book.html", context)

def delete_book(request, id):
    # Get mood berdasarkan id
    book = Book.objects.get(pk = id)
    # Hapus mood
    book.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_book_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    author = strip_tags(request.POST.get("author"))
    price = request.POST.get("price")
    image = request.POST.get("image")
    user = request.user

     # Validate input - check if the sanitized input is not empty
    if not name.strip():
        return JsonResponse({"error": "Name cannot be empty or invalid"}, status=400)
    if not author.strip():
        return JsonResponse({"error": "Author cannot be empty or invalid"}, status=400)

    new_book = Book(
        name=name, author=author,
        price=price, image=image,
        user=user
    )
    new_book.save()

    return HttpResponse(b"CREATED", status=201)