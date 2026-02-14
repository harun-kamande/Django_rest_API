from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions,authentication
from .serializers import ProductSerializer
from .models import Product
# Create your views here.

class ProductView(APIView):
    def get(self, request):
        my_products = Product.objects.all()
        serializer = ProductSerializer(my_products, many=True)

        return Response({"message": "Product View GET method", "data": serializer.data, "status": status.HTTP_200_OK})
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            my_products = Product.objects.all()
            serializer = ProductSerializer(my_products, many=True)
            return Response({"message": "Product View POST method", "data": serializer.data, "status": status.HTTP_201_CREATED})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        product_id = request.data.get('id')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            my_products = Product.objects.all()
            serializer = ProductSerializer(my_products, many=True)
            return Response({"message": "Product View PUT method", "data": serializer.data, "status": status.HTTP_200_OK})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        product_id = request.data.get('id')
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return Response({"message": "Product View DELETE method", "data": f"Product with id {product_id} deleted", "status": status.HTTP_200_OK})
 
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request):
        product_id = request.data.get('id')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            my_products = Product.objects.all()
            serializer = ProductSerializer(my_products, many=True)
            return Response({"message": "Product View PATCH method", "data": serializer.data, "status": status.HTTP_200_OK})
        return Response({"message": "Product View PATCH method", "data": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})