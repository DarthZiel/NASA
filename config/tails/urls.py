from django.urls import path
from .views import DeepZoomImageListCreateView, DeepZoomImageDetailView, get_tile

urlpatterns = [
    path("deepzoom/", DeepZoomImageListCreateView.as_view(), name="deepzoom-list-create"),
    path("deepzoom/<int:pk>/", DeepZoomImageDetailView.as_view(), name="deepzoom-detail"),
    path("deepzoom/<int:pk>/tile/<int:z>/<int:x>_<int:y>.png", get_tile, name="deepzoom-tile"),
]
