from django.contrib import admin

from apps.menu.models import Menu, DishMenu


class DishMenuInline(admin.TabularInline):
    model = DishMenu
    extra = 1


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['user', 'day_of_week', 'date_created']
    inlines = [DishMenuInline]
