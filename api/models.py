from django.db import models
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
class Customers(models.Model):
    username=models.CharField(max_length=200)
    age=models.DecimalField(decimal_places=2, max_digits=99)
    gender=models.TextField(null=False)
    country=models.TextField(max_length=900)

    def __str__(self):
        return f"{self.username}"