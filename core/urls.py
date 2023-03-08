from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from core.yasg import urlpatterns as docs_urls


urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/auth/", include("rest_framework.urls")),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path("api/users/", include("apps.users.urls")),
    path("api/menu/", include("apps.menu.urls")),
    path("api/dishes/", include("apps.dishes.urls")),
]

urlpatterns += docs_urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
