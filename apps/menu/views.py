from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.menu.serializers import MenuSerializer
from apps.menu.models import Menu
from apps.menu.permissions import IsOwnerOrAdminOrReadOnly


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all().order_by("date_created")
    serializer_class = MenuSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
