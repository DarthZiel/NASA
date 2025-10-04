# Документация API — DeepZoom

---

## 1. Список изображений (GET)

**URL**
```
GET https://e79a79efae0b.ngrok-free.app/api/deepzoom/
```

**Описание**  
Возвращает список всех записей `DeepZoomImage` (короткая информация + ссылка на `.dzi`).

**Пример ответа (200 OK)**
```json
[
    {
        "id": 2,
        "name": "sus",
        "dzi_path": "media/tiles/BlackMarble/image.dzi",
        "base_dir": "",
        "width": null,
        "height": null,
        "created_at": "2025-10-04T11:58:02.718467Z",
        "updated_at": "2025-10-04T11:58:02.718530Z",
        "dzi_url": "/media/tiles/sus/image.dzi",
        "image_url": "/media/tiles/sus/image_files"
    },
    {
        "id": 1,
        "name": "BlackMarble",
        "dzi_path": "media/tiles/BlackMarble/image.dzi",
        "base_dir": "",
        "width": null,
        "height": null,
        "created_at": "2025-10-04T11:39:38.460282Z",
        "updated_at": "2025-10-04T11:39:38.460351Z",
        "dzi_url": "/media/tiles/BlackMarble/image.dzi",
        "image_url": "/media/tiles/BlackMarble/image_files"
    }
]
```

---

## 2. Детальная запись изображения (GET)

**URL**
```
GET https://e79a79efae0b.ngrok-free.app/api/deepzoom/<id>/
```

**Описание**  
Возвращает подробную информацию для конкретного изображения `id`.

**Пример**
```
GET https://e79a79efae0b.ngrok-free.app/api/deepzoom/1/
```

**Пример ответа (200 OK)**
```json
{
    "id": 1,
    "name": "BlackMarble",
    "dzi_path": "media/tiles/BlackMarble/image.dzi",
    "base_dir": "",
    "width": null,
    "height": null,
    "created_at": "2025-10-04T11:39:38.460282Z",
    "updated_at": "2025-10-04T11:39:38.460351Z",
    "dzi_url": "/media/tiles/BlackMarble/image.dzi",
    "image_url": "/media/tiles/BlackMarble/image_files"
}
```

---

## 3. Прямой доступ к тайлу (пример)

Файлы тайлов и `.dzi` лежат в `MEDIA_URL`, поэтому фронт может запрашивать их напрямую как обычные изображения.

**Пример `.dzi`**
```
https://e79a79efae0b.ngrok-free.app/media/tiles/BlackMarble/image.dzi
```
**Запроса конкретного тайла**
```
https://e79a79efae0b.ngrok-free.app/media/tiles/BlackMarble/image_files/z/x_y.png
```

**Пример запроса конкретного тайла**
```
https://e79a79efae0b.ngrok-free.app/media/tiles/BlackMarble/image_files/13/9_11.png
```

**Ответ**
- `200 OK` → файл PNG  
- `404 Not Found` → если такого тайла нет  
