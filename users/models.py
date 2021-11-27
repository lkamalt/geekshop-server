from django.db import models
# Здесь находятся модели приложения auth
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Переопределяем модель пользователей
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
