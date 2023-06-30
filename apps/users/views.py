from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from apps.users.models import User, Position
from apps.users.permissions import IsOwnerOrAdminOrReadOnly
from apps.users.serializers import (
    UserSerializer,
    UserRegisterSerializer,
    PositionSerializer,
)


class UserMeAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        if not request.user.is_authenticated:
            return Response('Not authenticated', status=401)

        data = self.get_serializer(request.user).data

        return Response(data=data, status=200)
    


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
