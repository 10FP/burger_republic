from django.db import models

# Create your models here.
class Hamburger(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='hamburgers/', null=True, blank=True)