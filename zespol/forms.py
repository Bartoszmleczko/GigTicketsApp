from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from zespol.models import *
from django.views.generic import UpdateView
from django.urls import reverse_lazy

class SignUpForm(UserCreationForm):
    imię = forms.CharField(max_length=30, required=True)
    nazwisko = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'imię', 'nazwisko', 'email', 'password1', 'password2', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=( 'imie', 'nazwisko', 'email', )
