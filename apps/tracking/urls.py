from django.urls import path

from apps.tracking.views import TrackingListCreateView, TrackingUpdateDeleteView, UserTrackingViewSet

urlpatterns = (
    path('tracking/', TrackingListCreateView.as_view(), name="tracking"),
    path('tracking/<int:pk>/', TrackingUpdateDeleteView.as_view(), name="tracking"),
    path('visit/', UserTrackingViewSet.as_view({'get': 'list'}), name="visit"),
)
