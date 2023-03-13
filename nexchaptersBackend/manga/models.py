from django.db import models

# Create your models here.
class Manga(models.Model):
    title= models.CharField(max_length=50, null=False)
    image= models.CharField(max_length=200, default="")
    link = models.CharField(max_length=200, default="")
    total_chapters= models.IntegerField()
    current_chapter= models.IntegerField(default=0) 