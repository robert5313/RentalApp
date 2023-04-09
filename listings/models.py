from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.title