import django_filters

from apps.dishes.models import Dish, Ingredient


class DishFilter(django_filters.FilterSet):
    ingredients = django_filters.ModelMultipleChoiceFilter(
        field_name='ingridients__ingredient__title',
        to_field_name='title',
        queryset=Ingredient.objects.all()
    )

    class Meta:
        model = Dish
        fields = ['ingredients']
