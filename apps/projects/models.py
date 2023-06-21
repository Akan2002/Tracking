from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    link = models.URLField(verbose_name='Ссылка')
    team_lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name='led_projects', null=True, verbose_name='Тим лид')
    assignee = models.ManyToManyField(User, related_name='assigned_projects', verbose_name='Исполнитель')
    participants = models.ManyToManyField(User, blank=True, verbose_name='Участники')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
