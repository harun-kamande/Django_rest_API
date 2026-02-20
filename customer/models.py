from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Customers(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    # def get_customers(self):
    #     return User.objects.filter(user=self)