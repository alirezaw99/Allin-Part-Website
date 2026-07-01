import os

from django.conf import settings


def get_tumbnail_upload_path(instance, filename):
    folder = instance.part_number
    ext = filename.split(".")[-1]
    path = os.path.join("images", "tumbnails", folder)
    filename = f"{folder}-thumbnail.{ext}"

    return os.path.join(path, filename)


def get_images_upload_path(instance, filename):
    folder = instance.part.part_number
    ext = filename.split(".")[-1]
    rel_base = os.path.join("images", folder)
    abs_base = os.path.join(settings.MEDIA_ROOT, rel_base)

    id = 0
    while True:
        fname = f"{folder}-{id}.{ext}"
        if not os.path.isfile(os.path.join(abs_base, fname)):
            return os.path.join(rel_base, fname)
        id += 1
