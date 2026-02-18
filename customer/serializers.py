from rest_framework import serializers
from .models import Customers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        # fields=['id','username','age','gender','country','password']
        fields = '__all__'
        
