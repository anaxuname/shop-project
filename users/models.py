from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name='Номер телефона', null=True, blank=True)
    country = models.CharField(max_length=50, verbose_name='Страна', null=True, blank=True)
    avatar = models.ImageField(upload_to='user/', verbose_name='Аватар', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []