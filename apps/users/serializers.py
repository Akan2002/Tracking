from rest_framework import serializers
from .models import Position, User

COMMON_FIELDS = ["id", "username", "first_name", "last_name", "password", "position"]


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ("id", "title")


class UserSerializer(serializers.ModelSerializer):
    position_title = serializers.ReadOnlyField(source="position.title")

    class Meta:
        model = User
        COMMON_FIELDS_COPY = COMMON_FIELDS.copy()
        COMMON_FIELDS_COPY.remove("password")
        fields = COMMON_FIELDS_COPY + ["position_title"]



class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    position_title = serializers.ReadOnlyField(source="position.title")

    class Meta:
        model = User
        fields = COMMON_FIELDS + ["password_confirm", "position_title", "is_superuser"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"read_only": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        password_confirm = validated_data.pop("password_confirm")

        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = COMMON_FIELDS
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
            "username": {"required": False},
        }

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.position = validated_data.get("position", instance.position)

        password = validated_data.get("password")
        if password:
            instance.set_password(password)

        instance.save()
        return instance

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response.setdefault(
            "position_title", instance.position.title
            if instance.position else None
        )
        return response
