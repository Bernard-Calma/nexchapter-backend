from django.db import models

# Create your models here.
class Manga(models.Model):
    title: models.CharField()
    image: models.CharField()
    total_chapters: models.IntegerField()
    current_chapter: models.IntegerField()
