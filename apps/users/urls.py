from rest_framework.routers import DefaultRouter as DR
from django.urls import path
from apps.users.views import (
    UserView, UserPositionView, RegistrationView, AuthenticationView
)

router = DR()

router.register('user', UserView)
router.register('position', UserPositionView)

urlpatterns = [
    path('reg/', RegistrationView.as_view()),
    path('auth/', AuthenticationView.as_view()),
]

urlpatterns += router.urls