from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.hashers import check_password

from apps.users.models import User, UserPosition
from apps.users.serializers import (
    UserSerializer, UserPositionSerializer, 
    RegistrationSerializer, AuthenticationSeriallizer
)

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserPositionView(ModelViewSet):
    queryset = UserPosition.objects.all()
    serializer_class = UserPositionSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if User.objects.filter(username=username).exists():
            return Response(
                {'message': 'Пользоваетель с таким именем существует'},
                status=status.HTTP_403_FORBIDDEN
            )
        user = User.objects.create_user(
            username=username,
            password=password,
        )

        token = RefreshToken.objects.create(user=user)
        return Response({'token': token.key}, status.HTTP_201_CREATED)
    

class AuthenticationView(APIView):
    def post(self, request):
        serializer = AuthenticationSeriallizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username).first()

        if user is not None:
            if check_password(password, user.password):
                token, _ = RefreshToken.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response({"error": 'Пароль не верный'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": 'Такой пользователь не существует'}, status=status.HTTP_400_BAD_REQUEST)