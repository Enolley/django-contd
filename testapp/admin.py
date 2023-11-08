from django.contrib import admin

from .models import Students, Slider

from django.contrib.auth.admin import UserAdmin

from testapp.form import CustomUserChangeForm, CustomUserCreationForm

from testapp.models import CustomUser

# Register your models here.

admin.site.register(Students)
admin.site.register(Slider)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(CustomUser, CustomUserAdmin)
