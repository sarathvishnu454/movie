from django.db import models


# Create your models here.
class movies(models.Model):
    name = models.CharField(max_length=150)
    discription = models.CharField(max_length=500)
    year = models.IntegerField()
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name
