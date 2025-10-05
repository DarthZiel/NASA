from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Annotation
from tails.models import DeepZoomImage

class AnnotationCreateSerializer(serializers.ModelSerializer):
    original_image = serializers.PrimaryKeyRelatedField(
        queryset=DeepZoomImage.objects.all()
    )

    class Meta:
        model = Annotation
        fields = ['original_image', 'text', 'polygon']
        read_only_fields = ['image_url', 'user', 'created_at']

    def create(self, validated_data):
        # Автоматически устанавливаем пользователя из запроса
        validated_data['user'] = self.context['request'].user
        # Устанавливаем image_url на основе original_image
        validated_data['image_url'] = validated_data['original_image'].image_url
        return super().create(validated_data)

    def validate(self, data):
        # Опциональная валидация: проверяем, что polygon — валидный JSON
        if not isinstance(data['polygon'], (dict, list)):
            raise serializers.ValidationError("Поле polygon должно быть валидным JSON (список или словарь).")
        return data

class AnnotationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Возвращает username
    original_image = serializers.StringRelatedField()  # Возвращает name из DeepZoomImage

    class Meta:
        model = Annotation
        fields = ['id', 'user', 'original_image', 'image_url', 'text', 'polygon', 'created_at']