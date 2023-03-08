from rest_framework.routers import DefaultRouter

from apps.dishes.views import IngredientViewSet, DishViewSet


router = DefaultRouter()

router.register("ingredients", IngredientViewSet, basename="ingredients")
router.register('dishes', DishViewSet, basename="dishes")

urlpatterns = []
urlpatterns += router.urls
