from django.db import models

# Create your models here.
class DeepZoomImage(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Название изображения (например, Mars Crater)")
    dzi_path = models.FilePathField(path="media/tiles", match=".*\.dzi$", recursive=True, max_length=500)
    base_dir = models.FilePathField(path="media/tiles", match=".*_files$", recursive=True, max_length=500)
    width = models.PositiveIntegerField(help_text="Ширина исходного изображения в пикселях", blank=True, null=True)
    height = models.PositiveIntegerField(help_text="Высота исходного изображения в пикселях", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    @property
    def dzi_url(self):
        """Возвращает URL для фронта."""
        from django.conf import settings
        return f"{settings.MEDIA_URL}tiles/{self.name}/image.dzi"

    @property
    def image_url(self):
        from django.conf import settings
        return f"{settings.MEDIA_URL}tiles/{self.name}/image_files"