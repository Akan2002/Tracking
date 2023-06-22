from django.db import models
from django.contrib.auth.models import AbstractUser


class UserPosition(models.Model):
    position = models.CharField(max_length=127, verbose_name='Позиция')

    def __str__(self) -> str:
        return self.position
    
    class Meta:
        verbose_name = 'Пользователь и позиция'
        verbose_name_plural = 'Пользователь и позиции'

    
class User(AbstractUser):
    position = models.ForeignKey(
        UserPosition, on_delete=models.CASCADE, related_name='users_position', blank=True, null=True
)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        
