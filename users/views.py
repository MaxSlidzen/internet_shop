from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm, UserLoginForm
from users.models import User


class UserLoginView(LoginView):
    model = User
    form_class = UserLoginForm


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        return self.request.user
