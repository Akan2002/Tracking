from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings

from core.yasg import urlpatterns as docs_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('apps.users.urls')),
    path('api1/', include('apps.projects.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('auth/', include('rest_framework.urls')),
]




urlpatterns += docs_urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

