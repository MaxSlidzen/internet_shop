from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserRegisterView, UserProfileView, UserLoginView, verify, generate_password

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('verify_<str:verify_key>/', verify, name='verify'),
    path('reset/', generate_password, name='generate_password'),
]
