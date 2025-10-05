from rest_framework import generics
from .models import DeepZoomImage
from .serializers import DeepZoomImageSerializer
from django.http import FileResponse, Http404
import os


class ResponseHeaderMixin:
    """Миксин для добавления кастомных заголовков в ответы."""

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        response['ngrok-skip-browser-warning'] = 'true'  # Добавь любой заголовок
        # Или другие: response['Custom-Header'] = 'value'
        return response


class DeepZoomImageListCreateView(ResponseHeaderMixin, generics.ListCreateAPIView):
    queryset = DeepZoomImage.objects.all()
    serializer_class = DeepZoomImageSerializer


class DeepZoomImageDetailView(generics.RetrieveAPIView):
    queryset = DeepZoomImage.objects.all()
    serializer_class = DeepZoomImageSerializer
