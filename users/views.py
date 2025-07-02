from django.contrib.auth.views import LoginView
from django.conf import settings
from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import RegisterForm, LoginForm
from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:login')


    def form_valid(self, form):
        response = super().form_valid(form)
        # Отправка приветственного письма
        send_mail(
            'Добро пожаловать в SkyStore!',
            'Спасибо за регистрацию в нашем магазине.',
            settings.DEFAULT_FROM_EMAIL,
            [form.cleaned_data['email']],
            fail_silently=False,
        )
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Поля формы:", list(context['form'].fields.keys()))  # Отладочный вывод
        return context

class CustomLoginView(LoginView):
    # form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:home')


class CustomLogoutView(LogoutView):
    next_page = 'catalog:home'
