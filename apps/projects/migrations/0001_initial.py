# Generated by Django 4.2.2 on 2023-06-27 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=127, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                ("link", models.URLField(verbose_name="Ссылка")),
                (
                    "assignee",
                    models.ManyToManyField(
                        related_name="assigned_projects",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Исполнитель",
                    ),
                ),
                (
                    "participants",
                    models.ManyToManyField(
                        blank=True,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Участники",
                    ),
                ),
                (
                    "team_lead",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="led_projects",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Тим лид",
                    ),
                ),
            ],
            options={
                "verbose_name": "Проект",
                "verbose_name_plural": "Проекты",
            },
        ),
    ]
