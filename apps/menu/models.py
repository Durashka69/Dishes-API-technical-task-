from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.models import User

from apps.menu.choices import EATING_TIME, DAY_CHOICES

from apps.dishes.models import Dish


class Menu(models.Model):
    user = models.OneToOneField(
        User, 
        verbose_name=_("user"), 
        related_name="пользователь",
        on_delete=models.CASCADE
    )
    day_of_week = models.CharField(
        choices=DAY_CHOICES, max_length=20, verbose_name="День недели"
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"меню пользователя {self.user.email}"

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = 'Меню'


class DishMenu(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="menu")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="dishes")
    eating_time = models.CharField(max_length=7, choices=EATING_TIME)
