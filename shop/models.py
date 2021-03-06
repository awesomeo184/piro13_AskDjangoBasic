from django.conf import settings
from django.db import models

from Askdjango.utils import uuid_upload_to


class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to)
    price = models.PositiveIntegerField()
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.pk}> {self.name}'

# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# blog의 related_name 충돌이 일어남