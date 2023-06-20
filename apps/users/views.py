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
    UserSerializer, AuthenticationSerializer,
    
)

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserPositionView(ModelViewSet):
    queryset = UserPosition.objects.all()
    serializer_class = UserPositionSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user_id': user.id,
                'username': user.username,
                'position': user.position.position,
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }, status=201)
        return Response(serializer.errors, status=400)


class AuthenticationView(APIView):
    def post(self, request):
        serializer = AuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=200)
        return Response(serializer.errors, status=400)