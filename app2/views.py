from django.shortcuts import render


def Home(request):
    return render(request, 'hhome.html', {'navbar': 'settings'})
# Create your views here.
