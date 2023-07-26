from datetime import date

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

from apps.tracking.models import Tracking
from apps.tracking.serializers import TrackingSerializer
from apps.tracking.filters import TrackingFilter


class TrackingListCreateView(generics.ListCreateAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TrackingFilter
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        current_date = date.today()
        first_day_of_month = date(current_date.year, current_date.month, 1)

        self.filterset_class.base_filters['date_from'].default = first_day_of_month
        self.filterset_class.base_filters['date_to'].default = current_date

        queryset = super().get_queryset()
        
        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(user__username=username)

        return queryset


class TrackingUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer
    permission_classes = (IsAdminUser,)


class UserTrackingViewSet(ReadOnlyModelViewSet):
    serializer_class = TrackingSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = TrackingFilter

    def get_queryset(self):
        user = self.request.user
        queryset = Tracking.objects.filter(user=user)
        return queryset
