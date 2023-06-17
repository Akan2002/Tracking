from rest_framework import serializers, exceptions
from .models import UserPosition, User


class UserPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPosition
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    position = UserPositionSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'position')


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    def validated_password(self, value):
        if len(value) < 6:
            raise exceptions.ValidationError('Пароль слишком короткий')                  
        elif len(value) > 20:
            raise exceptions.ValidationError('Пароль слишком длинный')
        return value

class AuthenticationSeriallizer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
