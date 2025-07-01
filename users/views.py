from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import RegisterForm, LoginForm
from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Отправка приветственного письма
        send_mail(
            'Добро пожаловать в SkyStore!',
            'Спасибо за регистрацию в нашем магазине.',
            self.request.email,  # или DEFAULT_FROM_EMAIL из settings
            [form.cleaned_data['email']],
            fail_silently=False,
        )
        return response


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


class CustomLogoutView(LogoutView):
    next_page = 'catalog:home'
