from rest_framework import serializers
from .models import User,Customers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','age']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields=['id','username','gender','age','country']

