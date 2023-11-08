from django.urls import path
from . import views

app_name = "testapp"
urlpatterns = [
    path('', views.Test, name="Test"),
    path('contact', views.contact, name="Contact"),
    path('about', views.about, name="About"),
    path('add', views.add, name="Add"),
    path('view', views.view, name="View"),
    path('sliders', views.sliders, name="Sliders"),

    path('delete/<id>', views.delete, name="Delete"),
    path('insert', views.insert, name="Insert"),
    path('edit/<id>', views.edit, name="Edit"),

    path('search', views.search, name="Search"),

    path('register', views.SignUp.as_view(), name="Register"),
    path('login', views.UserLogin.as_view(), name="Login"),
    path('logout', views.Logout, name="Logout")
]
