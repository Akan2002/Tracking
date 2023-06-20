from rest_framework.routers import DefaultRouter as DR

from apps.projects.views import ProjectsView

router = DR()

router.register('projects', ProjectsView, basename='projects')

urlpatterns2 = []

urlpatterns2 += router.urls