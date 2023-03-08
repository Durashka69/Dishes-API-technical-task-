import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


from django.conf import settings

from apps.dishes.models import Dish, Ingredient, DishIngridient
