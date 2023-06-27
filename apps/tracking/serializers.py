from rest_framework import serializers

from apps.tracking.models import Tracking


class TrackingSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, source="user.username")

    class Meta:
        model = Tracking
        fields = ("id", "user", "username", "coming_time", "is_late")
        read_only_fields = ("is_late",)
