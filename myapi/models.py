from django.db import models

# Create your models here.
class Nickname(models.Model):
    name = models.CharField(max_length=60)
    petname = models.CharField(max_length=60)
    def __str__(self):
        return self.name