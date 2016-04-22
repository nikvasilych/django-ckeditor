from django.utils.functional import LazyObject
from django.core.files.storage import get_storage_class
from django.conf import settings

class ImageStorage(LazyObject):
    def _setup(self):
        self._wrapped = get_storage_class(getattr(settings, 'CKEDITOR_UPLOAD_STORAGE', settings.DEFAULT_FILE_STORAGE))()

image_storage = ImageStorage()