from rest_framework import serializers

from apps.projects.models import Projects

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = (
            'id', 'name', 'description', 'link', 'team_lead', 'assignee', 'participants'
        )
