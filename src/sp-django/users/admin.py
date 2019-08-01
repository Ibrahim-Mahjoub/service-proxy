from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SPUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    """
    Custom user admin class.
    """
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm 

# Register your models here.
admin.site.register(SPUser, CustomUserAdmin)    
