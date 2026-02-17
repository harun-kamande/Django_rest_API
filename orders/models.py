from django.db import models
from customer.models import Customers
# Create your models here.

class Orders(models.Model):
    customer=models.ForeignKey(Customers, on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    order_amount=models.DecimalField(max_digits=10, decimal_places=2)
    order_status=models.CharField(max_length=20)
    order_description=models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"
    
    