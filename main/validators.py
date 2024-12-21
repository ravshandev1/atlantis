from django.core.exceptions import ValidationError
import os
from django.conf import settings
import uuid


def img_validator(image):
    max_size = settings.IMG_SIZE * 1024 * 1024  # 5 MB ni baytlarda
    if image.size > max_size:
        raise ValidationError(
            f"Fayl hajmi {settings.IMG_SIZE} MB dan oshmasligi kerak. Hozirgi hajm: {image.size / (1024 * 1024):.2f} MB")
    valid_extensions = ['.jpg', '.jpeg', '.png']
    ext = os.path.splitext(image.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError(f"Fayl kengaytmasi quyidagilardan biri bo'lishi kerak: {', '.join(valid_extensions)}.")


def custom_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    folder_name = instance.__class__.__name__.lower()
    return os.path.join(folder_name, filename)