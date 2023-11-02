from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Students, Slider


def Test(request):
    return render(request, 'pages/home.html', {'navbar': 'home'})


def contact(request):
    return render(request, 'Tes.html', {'navbar': 'contact'})


def about(request):
    return render(request, 'about.html', {'navbar': 'about'})


def add(request):
    return render(request, 'add.html', {'navbar': 'add'})


def view(request):
    # retrieve data
    data = Students.objects.all()
    return render(request, 'view.html', {'navbar': 'view', 'data': data})


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
    return render(request, 'sliders.html', {'navbar' : 'slider', 'slides': slides}, )


