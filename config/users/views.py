from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Annotation
from .serializers import AnnotationCreateSerializer, AnnotationSerializer

class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return AnnotationCreateSerializer
        return AnnotationSerializer

    def perform_create(self, serializer):
        # Автоматически устанавливаем пользователя
        serializer.save(user=self.request.user)