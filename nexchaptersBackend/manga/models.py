from django.db import models

# Create your models here.
class Manga(models.Model):
    title: models.CharField(max_length=200, null=True)
    image: models.CharField(max_length=200, null=True)
    total_chapters: models.IntegerField()
    current_chapter: models.IntegerField()

    def __str__(self):
        return self.title