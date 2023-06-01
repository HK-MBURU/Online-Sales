from django import forms
from django.forms import ModelForm
from .models import Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
