from django.db import models

# Create your models here.
class Manga(models.Model):
    title= models.CharField(max_length=100, null=False)
    image= models.CharField(max_length=200, default="")
    link = models.CharField(max_length=200, default="")
    total_chapters= models.IntegerField(default=0)
    current_chapter= models.IntegerField(default=0) 
    user = models.ForeignKey('user.User',on_delete=models.CASCADE, null=False) 