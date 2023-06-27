from django.urls import path

from apps.tracking.views import TrackingListCreateView, TrackingUpdateDeleteView

urlpatterns = (
    path('tracking/', TrackingListCreateView.as_view(), name="tracking"),
    path('tracking/<int:pk>/', TrackingUpdateDeleteView.as_view(), name="tracking"),
)
