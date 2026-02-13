from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions,authentication


from .models import Customers
from .serializers import CustomerSerializer



# Create your views here.
class CustomerView(APIView):
 
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


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