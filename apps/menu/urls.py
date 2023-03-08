from rest_framework.routers import DefaultRouter

from apps.menu.views import MenuViewSet


router = DefaultRouter()

router.register("", MenuViewSet, basename='menu')

urlpatterns = []
urlpatterns += router.urls
