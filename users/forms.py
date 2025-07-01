from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Телефон')
    country = forms.CharField(label='Страна')

    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'country', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
