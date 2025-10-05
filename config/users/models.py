from django.conf import settings
from django.db import models

# Create your models here.
class Annotation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="annotations"
    )
    original_image = models.ForeignKey(
        "tails.DeepZoomImage",   # Привязка к твоей модели DeepZoomImage
        on_delete=models.CASCADE,
        related_name="annotations"
    )

    image_url = models.CharField(max_length=500)

    text = models.TextField(help_text="Текстовое описание метки")
    polygon = models.JSONField(help_text="Координаты полигона (относительно тайла или всего изображения)")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Annotation {self.id} on {self.image.name} by {self.user}"