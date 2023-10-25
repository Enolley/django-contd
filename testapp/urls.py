from django.urls import path
from . import views


app_name = "testapp"
urlpatterns = [
    path('', views.Test, name="Test"),
    path('contact', views.contact, name="Contact"),
    path('about', views.about, name="About")
]