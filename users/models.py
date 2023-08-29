from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    phone = models.CharField(max_length=35, unique=True, **NULLABLE, verbose_name='номер телефона')
    country = models.CharField(max_length=50, **NULLABLE, verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
