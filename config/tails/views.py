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


def get_tile(request, pk, z, x, y):
    from .models import DeepZoomImage
    try:
        obj = DeepZoomImage.objects.get(pk=pk)
    except DeepZoomImage.DoesNotExist:
        raise Http404

    tile_path = os.path.join(obj.base_dir, str(z), f"{x}_{y}.png")
    if not os.path.exists(tile_path):
        raise Http404

    return FileResponse(open(tile_path, "rb"), content_type="image/png")
