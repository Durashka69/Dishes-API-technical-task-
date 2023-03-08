from django.contrib import admin
from apps.dishes.models import Ingredient, Dish, DishIngridient


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)


class DishIngridientInline(admin.TabularInline):
    model = DishIngridient
    extra = 1


class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    inlines = [DishIngridientInline]


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Dish, DishAdmin)
