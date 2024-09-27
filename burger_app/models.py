from django.db import models

# Create your models here.
class Hamburger(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='hamburgers/', null=True, blank=True)

class MenuHamburger(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='menu_hamburgers/', null=True, blank=True)

class MenuFries(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='menu_fries/', null=True, blank=True)

class MenuDrink(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='menu_drinks/', null=True, blank=True)



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.message



class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email