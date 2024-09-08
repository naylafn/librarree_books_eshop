from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'application' : 'Librarree',
        'name': 'Nayla Farah Nida',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)