import os
import pyvips
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from pathlib import Path
from tails.models import DeepZoomImage

class Command(BaseCommand):
    help = "Генерация Deep Zoom (DZI) изображения и сохранение записи в БД"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            required=False,
            help="Путь к исходному изображению (tif, jpg, png). Если не указан, берётся файл из той же папки."
        )
        parser.add_argument("--name", type=str, required=True, help="Имя для сохранения (например, MarsCrater)")

    def handle(self, *args, **options):
        name = options["name"]
        user_path = options.get("path")

        # Папка, где лежит сам скрипт
        script_dir = Path(__file__).resolve().parent

        # 🔹 Если путь не указан → ищем первый tif/jpg/png рядом со скриптом
        if not user_path:
            for ext in (".tif", ".tiff", ".jpg", ".jpeg", ".png"):
                found = list(script_dir.glob(f"*{ext}"))
                if found:
                    input_path = found[0]
                    self.stdout.write(self.style.NOTICE(f"Файл не указан — найден автоматически: {input_path.name}"))
                    break
            else:
                raise CommandError("Не найдено ни одного изображения (.tif/.jpg/.png) рядом со скриптом.")
        else:
            # 🔹 Если указан относительный путь или просто имя файла
            input_path = Path(user_path)
            if not input_path.is_absolute():
                input_path = script_dir / input_path

        # Проверяем, что файл реально существует
        if not input_path.exists():
            raise CommandError(f"Файл не найден: {input_path}")

        # Папка назначения в MEDIA_ROOT
        output_dir = Path(settings.MEDIA_ROOT) / "tiles" / name
        output_dir.mkdir(parents=True, exist_ok=True)

        self.stdout.write(self.style.NOTICE(f"Загружаем изображение: {input_path}"))

        # Загружаем без полной загрузки в RAM
        image = pyvips.Image.new_from_file(str(input_path), access="sequential")

        width, height = image.width, image.height
        self.stdout.write(f"Размер изображения: {width} x {height}")

        dzi_base = output_dir / "image"

        # Генерация DeepZoom
        self.stdout.write("Генерация DZI пирамиды...")
        image.dzsave(
            str(dzi_base),
            tile_size=256,
            overlap=0,
            depth="onepixel",
            suffix=".png",
            properties=True,
        )

        dzi_path = output_dir / "image.dzi"
        base_dir = output_dir / "image_files"

        if not dzi_path.exists():
            raise CommandError("Ошибка: DZI файл не создан!")

        # Создаём или обновляем запись в БД
        deepzoom_obj, created = DeepZoomImage.objects.get_or_create(
            name=name,
            defaults={
                "dzi_path": str(dzi_path),
                "base_dir": str(base_dir),
                "width": width,
                "height": height,
            },
        )

        if not created:
            self.stdout.write(self.style.WARNING(f"⚠ Запись с именем '{name}' уже существует, обновляю данные."))
            deepzoom_obj.dzi_path = str(dzi_path)
            deepzoom_obj.base_dir = str(base_dir)
            deepzoom_obj.width = width
            deepzoom_obj.height = height
            deepzoom_obj.save()

        self.stdout.write(self.style.SUCCESS(f"✅ DZI успешно создан и сохранён в БД: {deepzoom_obj.name}"))
