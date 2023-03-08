from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, unique=True, verbose_name="email")
    first_name = models.CharField(max_length=255, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=255, blank=True, verbose_name="Фамилия")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    is_staff = models.BooleanField(default=False, verbose_name="Является ли персоналом")
    is_superuser = models.BooleanField(
        default=False, verbose_name="Является ли суперпользователем"
    )
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
