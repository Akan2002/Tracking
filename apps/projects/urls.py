from rest_framework.routers import DefaultRouter as DR

from apps.projects.views import ProjectView

router = DR()

router.register('project', ProjectView, basename='projects')

urlpatterns = []

urlpatterns += router.urls