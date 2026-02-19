from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions,authentication
from .serializers import OrderSerializer
from .models import Orders
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
# Create your views here.

class OrdersView(APIView):
    def get(self, request):
        get_orders = Orders.objects.all()
        serializer = OrderSerializer(get_orders, many=True)
        return Response({"message": "Orders View GET method", "data": serializer.data, "status": status.HTTP_200_OK})

    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            get_orders = Orders.objects.all()
            serializer = OrderSerializer(get_orders, many=True)
        return Response({"message": "Orders View POST method", "data": serializer.data, "status": status.HTTP_201_CREATED})
    
    def put(self,request):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            get_orders = Orders.objects.all()
            serializer = OrderSerializer(get_orders, many=True)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Orders View PUT method", "data": serializer.data, "status": status.HTTP_200_OK})
    
    def delete(self,request):
            order_id = request.data.get('id')
            try:
                order = Orders.objects.get(id=order_id)
                order.delete()
            except Orders.DoesNotExist:
                return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request):
        order_id = request.data.get('id')
        try:
            order = Orders.objects.get(id=order_id)
        except Orders.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            get_orders = Orders.objects.all()
            serializer = OrderSerializer(get_orders, many=True)
            return Response({"message": "Orders View PATCH method", "data": serializer.data, "status": status.HTTP_200_OK})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)