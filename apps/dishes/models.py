from django.db import models
from django.utils.translation import gettext_lazy as _


class Ingredient(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ингридиент"
        verbose_name_plural = "Ингридиенты"


class Dish(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название блюда")
    description = models.TextField(verbose_name="Описание")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class DishIngridient(models.Model):
    dish = models.ForeignKey(
        Dish, 
        related_name="ingridients",
        on_delete=models.CASCADE, 
        verbose_name="блюдо"
    )
    ingredient = models.ForeignKey(
        Ingredient,
        related_name="dishes", 
        on_delete=models.CASCADE
    )
    weight = models.PositiveSmallIntegerField(verbose_name="Граммаж")

    def __str__(self) -> str:
        return f"{self.ingredient.title} -- {self.weight} -- {self.dish.title}"

    class Meta:
        verbose_name = "Ингридиент блюда"
        verbose_name_plural = "Ингридиенты блюда"
