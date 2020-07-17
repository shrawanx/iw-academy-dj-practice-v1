import uuid

from django.db import models


def file_path(_, filename):
    # image.jpg
    extension = filename.split('.')[-1]
    unique_id = uuid.uuid4().hex

    new_file_name = 'sub/abcd/bcd/' + unique_id + '.' + extension
    return new_file_name


class FileModel(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to=file_path)
