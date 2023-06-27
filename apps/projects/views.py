from rest_framework.viewsets import ModelViewSet

from apps.projects.permissions import IsAdminOrReadOnly


from apps.projects.serializers import (
    ResponseProjectSerializer
)

from apps.projects.models import Project

class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ResponseProjectSerializer
    permission_classes = (IsAdminOrReadOnly,)
