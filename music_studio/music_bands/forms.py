from django import forms
from .models import Band
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'genre', 'year_formed', 'biography']



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']