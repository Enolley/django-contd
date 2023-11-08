from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Students, Slider
from django.core.paginator import Paginator

from django.views.generic import CreateView
from . models import CustomUser
from .form import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required





def contact(request):
    return render(request, 'Tes.html', {'navbar': 'contact'})


def about(request):
    return render(request, 'about.html', {'navbar': 'about'})


def add(request):
    return render(request, 'add.html', {'navbar': 'add'})


def view(request):

    paginate = Paginator(Students.objects.all().order_by('name'), 2)
    page = request.GET.get('page')
    data = paginate.get_page(page)
    return render(request, 'view.html', {'navbar': 'view', 'data': data})

#def view(request):
    #data = Students.objects.all()
    #return render(request, 'view.html', {'navbar': 'view', 'data': data})


def delete(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    messages.warning(request, 'Entry was successfully deleted')

    return redirect("/view")

def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if len(request.FILES) !=0:
            image = request.FILES['image']
        query = Students(name=name, email=email, phone=phone, image=image)
        query.save()
        messages.success(request, 'Data added successfully!')
        return redirect("/view")
    return redirect("/view")

def edit(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        image = request.FILES['image']

        student = Students.objects.get(id=id)

        student.name = name
        student.email = email
        student.phone = phone
        student.image = image

        student.save()
        messages.success(request, 'Data updated successfully!')
        return redirect("/view")

    student = Students.objects.get(id=id)
    return render(request, 'edit.html', {'student':student})

def sliders(request):
    slides = Slider.objects.all()
    return render(request, 'sliders.html', {'navbar' : 'slider', 'slides': slides})

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            student = Students.objects.filter(name__icontains=query)
            return render(request, 'search.html', {'data':student})

        return render(request, 'search.html')

#CLASS BASED VIEWS

class SignUp(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('testapp:Login')
    template_name = 'register.html'

class UserLogin(LoginView):
    template_name = 'login.html'

@login_required
def Test(request):
    return render(request, 'pages/home.html', {'navbar': 'home'})

def Logout(request):
    logout(request)
    return redirect('/login')