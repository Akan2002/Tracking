from rest_framework.viewsets import ModelViewSet


from apps.projects.serializers import (
    ProjectSerializer
)

from apps.projects.models import Project

class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
