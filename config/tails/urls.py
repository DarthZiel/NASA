from django.urls import path
from .views import DeepZoomImageListCreateView, DeepZoomImageDetailView

urlpatterns = [
    path("deepzoom/", DeepZoomImageListCreateView.as_view(), name="deepzoom-list-create"),
    path("deepzoom/<int:pk>/", DeepZoomImageDetailView.as_view(), name="deepzoom-detail"),

]
