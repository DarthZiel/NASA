from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnnotationViewSet

app_name = 'users'

router = DefaultRouter()
router.register(r'annotations', AnnotationViewSet, basename='annotation')

urlpatterns = [
    path('', include(router.urls)),
]