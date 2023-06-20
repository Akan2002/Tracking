from django.db import models
from django.contrib.auth.models import AbstractUser


class UserPosition(models.Model):
    position = models.CharField(max_length=127, verbose_name='Позиця')


class User(AbstractUser):
    position = models.ForeignKey(
        UserPosition, on_delete=models.CASCADE, related_name='users_position', blank=True, null=True
)
