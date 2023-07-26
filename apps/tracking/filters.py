from django_filters import rest_framework as filters

from apps.tracking.models import Tracking


class TrackingFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name="coming_time", lookup_expr="date__gte")
    date_to = filters.DateFilter(field_name="coming_time", lookup_expr="date__lte")
    username = filters.CharFilter(field_name="user__username", lookup_expr="exact")

    class Meta:
        model = Tracking
        fields = ["date_from", "date_to", "username"]
