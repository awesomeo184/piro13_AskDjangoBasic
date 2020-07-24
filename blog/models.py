from django.conf import settings
from django.db import models
from Askdjango.utils import uuid_upload_to


class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tag_set = models.ManyToManyField('Tag', blank=True)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)