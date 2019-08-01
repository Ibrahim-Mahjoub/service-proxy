from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SPUser

class CustomUserCreationForm(UserCreationForm):
    """
    User creation form (used in admin) for custom user model.
    """

    class Meta(UserCreationForm.Meta):
        model = SPUser
    

class CustomUserChangeForm(UserChangeForm):
    """
    User info change form (used in admin) for custom user model.
    """

    class Meta(UserChangeForm.Meta):
        model = SPUser

