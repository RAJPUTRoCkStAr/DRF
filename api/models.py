from django.db import models

# Create your models here.
class Adit(models.Model):
    name = models.CharField(max_length=28)
    marks = models.IntegerField()
    field = models.CharField(max_length=25)

    def __str__(self):
        return self.name