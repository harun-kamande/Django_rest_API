from rest_framework import serializers
from .models import Orders

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=['id','customer','order_date','order_amount','order_status','order_description']
        # fields = '__all__'