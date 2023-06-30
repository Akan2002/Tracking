from datetime import date

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
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
        return queryset


class TrackingUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer
    permission_classes = (IsAdminUser,)


