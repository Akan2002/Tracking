from django.urls import path
from rest_framework.routers import DefaultRouter as DR
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import (
    UserMeAPIView,
    UserListView,
    PositionView,
    RegistrationView,
)

router = DR()

router.register("positions", PositionView)

urlpatterns = [
    path("users/", UserListView.as_view()),
    path("users/me/", UserMeAPIView.as_view()),
    path("auth/register/", RegistrationView.as_view()),
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls
