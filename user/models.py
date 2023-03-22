from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, null=False, unique=True)
    email = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.username