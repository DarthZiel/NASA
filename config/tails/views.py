from rest_framework import generics
from .models import DeepZoomImage
from .serializers import DeepZoomImageSerializer
from django.http import FileResponse, Http404
import os


class DeepZoomImageListCreateView(generics.ListCreateAPIView):
    queryset = DeepZoomImage.objects.all()
    serializer_class = DeepZoomImageSerializer


class DeepZoomImageDetailView(generics.RetrieveAPIView):
    queryset = DeepZoomImage.objects.all()
    serializer_class = DeepZoomImageSerializer


