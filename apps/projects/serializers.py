from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.projects.models import Project

User = get_user_model()


class ProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "full_name")


class ResponseProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "link",
            "team_lead",
            "assignee",
            "participants",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        assignee_ids = representation.pop("assignee")
        participants_ids = representation.pop("participants")
        representation["assignee"] = ProjectUserSerializer(
            User.objects.filter(id__in=assignee_ids), many=True
        ).data
        representation["participants"] = ProjectUserSerializer(
            User.objects.filter(id__in=participants_ids), many=True
        ).data
        return representation
