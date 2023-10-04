from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """."""

    is_staff = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]
