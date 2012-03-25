from django.db import models

class Video(models.Model):
    path = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=200)
    content_type = models.CharField(max_length=200)