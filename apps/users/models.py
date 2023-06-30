from django.db import models
from django.contrib.auth.models import AbstractUser


class Position(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self) -> str:
        return self.position
    
    class Meta:
        verbose_name = "Позиция (должность)"
        verbose_name_plural = "Позиции (должности)"


class User(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="user",
        blank=True,
        null=True,
    )

    @property
    def full_name(self):
        return self.get_full_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
