from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from apps.users.serializers import UserSerializer
from apps.users.permissions import IsOwnerOrAdminOrReadOnly


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly,)
