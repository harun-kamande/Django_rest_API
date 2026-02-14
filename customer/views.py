from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions,authentication


from .models import Customers
from .serializers import CustomerSerializer



# Create your views here.
class CustomerView(APIView):
 
    # authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get(self, request):
        your_ip = request.META.get('REMOTE_ADDR')
        print(f"Your IP address is: {your_ip}")
        get_customers = Customers.objects.all()
        serializer = CustomerSerializer(get_customers, many=True)
        return Response({"message": "Customer View GET method", "data": serializer.data})
    
    def post(self, request):
        
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Customer View POST method", "data": serializer.data})
        return Response(serializer.errors, status=400)
    
    def put(self,request):
        customer_id = request.data.get('id')
        try:
            customer = Customers.objects.get(id=customer_id)
        except Customers.DoesNotExist:
            return Response({"error": "Customer not found"}, status=404)
        
        serializer = CustomerSerializer(customer, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Customer View PUT method", "data": serializer.data})
        return Response(serializer.errors, status=400)
    
    def delete(self,request):
        customer_id = request.data.get('id')
        try:
            customer = Customers.objects.get(id=customer_id)
            customer.delete()
            return Response({"message": "Customer View DELETE method", "data": f"Customer with id {customer_id} deleted"})
        except Customers.DoesNotExist:
            return Response({"error": "Customer not found"}, status=404)
        
    def patch(self,request):
        customer_id = request.data.get('id')
        try:
            customer = Customers.objects.get(id=customer_id)
        except Customers.DoesNotExist:
            return Response({"error": "Customer not found"}, status=404)
        
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Customer View PATCH method", "data": serializer.data})
        return Response(serializer.errors, status=400)