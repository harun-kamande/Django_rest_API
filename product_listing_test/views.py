from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions,authentication
from rest_framework.generics import ListAPIView
# Create your views here.
from customer.models import Customers
from django_filters.rest_framework import DjangoFilterBackend
from customer.serializers import CustomerSerializer


class ProductListingView(ListAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email','id','is_staff']  # Example filter fields

   