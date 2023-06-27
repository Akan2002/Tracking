from datetime import time
from datetime import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Tracking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="came_dates",
        verbose_name="Пользователь",
    )
    coming_time = models.DateTimeField(default=timezone.now)
    is_late = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        current_time = datetime.now().time()
        noon_time = time(12, 0, 0)

        if current_time >= noon_time:
            self.is_late = True

        super(Tracking, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Посещаемость"
        verbose_name_plural = "Посещаемость"
