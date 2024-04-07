from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    page_count = models.IntegerField()
    category = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=3, max_digits=5)
    image = models.ImageField()

    def __str__(self):
        return self.name
