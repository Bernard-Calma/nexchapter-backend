from django.db import models

class Manga(models.Model):
    title = models.CharField(255)
    img = models.CharField(255)
    totalChapters = models.IntegerField