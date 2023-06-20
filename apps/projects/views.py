from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from apps.projects.serializers import (
    ProjectsSerializer
)

from apps.projects.models import Projects

class ProjectsView(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    