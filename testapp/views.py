from django.shortcuts import render
from django.http import HttpResponse


def Test(request):
    return render(request, 'pages/home.html', {'navbar': 'home'})


def contact(request):
    return render(request, 'Tes.html', {'navbar': 'contact'})


def about(request):
    return render(request, 'about.html', {'navbar': 'about'})


def add(request):
    return render(request, 'add.html', {'navbar': 'add'})

def view(request):
    return render(request, 'view.html', {'navbar': 'view'})
