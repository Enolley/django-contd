from django.urls import path
from . import views

app_name = "app2"
urlpatterns = [
    path('', views.Home, name="Home")

]
