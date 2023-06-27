from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from apps.users.models import User, Position
from apps.users.permissions import IsOwnerOrAdminOrReadOnly
from apps.users.serializers import (
    UserSerializer,
    UserRegisterSerializer,
    UserUpdateSerializer,
    PositionSerializer
)


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsOwnerOrAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return UserUpdateSerializer
        return UserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly,)


class PositionView(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = (IsAdminUser,)


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
