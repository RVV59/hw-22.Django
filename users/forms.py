from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    phone = forms.CharField(label='Телефон', required=False)
    country = forms.CharField(label='Страна', required=False)
    avatar = forms.ImageField(label='Аватар', required=False)

    class Meta(UserCreationForm.Meta):
        """
        Наследуем Meta от родительского класса, чтобы сохранить его логику,
        и просто добавляем наши новые поля в список.
        """
        model = CustomUser
        fields = ('email', 'phone', 'country', 'avatar')


class LoginForm(AuthenticationForm):
    """
    Кастомная форма логина, использующая email вместо username.
    """
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'autofocus': True})
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'current-password'}),
    )