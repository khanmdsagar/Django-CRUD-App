from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 250)
    price = models.CharField(max_length = 250)
    quantity = models.CharField(max_length = 250, default = 1)
    date_of_creation = models.DateField()
