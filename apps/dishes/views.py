from django.utils.decorators import method_decorator

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from drf_yasg.utils import swagger_auto_schema

from apps.dishes.serializers import (
    DishSerializer, 
    IngredientSerializer
)
from apps.dishes.models import Ingredient, Dish
from apps.dishes.filters import DishFilter
from apps.dishes.permissions import IsAdminOrReadOnly


@method_decorator(name='list', decorator=swagger_auto_schema(tags=["ingredients"]))
@method_decorator(name='create', decorator=swagger_auto_schema(tags=["ingredients"]))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=["ingredients"]))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=["ingredients"]))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(tags=["ingredients"]))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=["ingredients"]))
class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAdminOrReadOnly,)


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = DishFilter
    search_fields = ["title"]
    ordering_fields = ["title"]
