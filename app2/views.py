from django.shortcuts import render


def Home(request):
    return render(request, 'hhome.html')
# Create your views here.
