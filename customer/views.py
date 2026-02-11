from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Customers
from .serializers import CustomerSerializer


# Create your views here.
class CustomerView(APIView):
    def get(self, request):
        get_customers = Customers.objects.all()
        serializer = CustomerSerializer(get_customers, many=True)
        return Response({"message": "Customer View GET method", "data": serializer.data})
    
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Customer View POST method", "data": serializer.data})
        return Response(serializer.errors, status=400)