from django.conf import settings
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm, UserLoginForm
from users.models import User
from users.services import send_verify_email


class UserLoginView(LoginView):
    model = User
    form_class = UserLoginForm


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save()
            new_user.verify_token = get_random_string(length=20)
            new_user.save()
            send_verify_email(new_user)
        return super().form_valid(form)


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        return self.request.user


def verify(request, verify_key):
    user_item = get_object_or_404(User, verify_token=verify_key)
    user_item.is_active = True
    user_item.save()
    return redirect(reverse('users:login'))


def generate_password(request):
    new_password = get_random_string(length=12)
    send_mail(
        'Смена пароля',
        f'Ваш новый пароль {new_password}',
        settings.EMAIL_HOST_USER,
        [request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))
