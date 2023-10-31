from django.shortcuts import render
from django.http import HttpResponse

from .models import Students


def Test(request):
    return render(request, 'pages/home.html', {'navbar': 'home'})


def contact(request):
    return render(request, 'Tes.html', {'navbar': 'contact'})


def about(request):
    return render(request, 'about.html', {'navbar': 'about'})


def add(request):
    return render(request, 'add.html', {'navbar': 'add'})

def view(request):
    #retrieve data
    data = Students.objects.all()
    return render(request, 'view.html', {'navbar': 'view', 'data': data})
