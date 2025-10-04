from rest_framework import serializers
from .models import DeepZoomImage


class DeepZoomImageSerializer(serializers.ModelSerializer):
    dzi_url = serializers.ReadOnlyField()
    image_url = serializers.ReadOnlyField()

    class Meta:
        model = DeepZoomImage
        fields = [
            "id",
            "name",
            "dzi_path",
            "base_dir",
            "width",
            "height",
            "created_at",
            "updated_at",
            "dzi_url",
            "image_url",
        ]
