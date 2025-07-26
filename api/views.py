from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Customers
from .serializer import UserSerializer, CustomerSerializer


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)


class CustomerView(APIView):
    def get(self, request):
        customers = Customers.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Message": "Success"})
        return JsonResponse(serializer.errors, status=400)


class CustomerDeleteView(APIView):
    def post(self, request):
        customer_id = request.data.get("id")

        if not customer_id:
            return JsonResponse({"error": "ID is required for deletion."}, status=400)

        try:
            customer = Customers.objects.get(id=customer_id)
            customer.delete()
            customers = Customers.objects.all()
            serializer = CustomerSerializer(customers, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Customers.DoesNotExist:
            return JsonResponse({"error": "Customer not found."}, status=404)


class CustomerUpdateView(APIView):
    def put(self, request):
        return self._update(request, partial=False)

    def patch(self, request):
        return self._update(request, partial=True)

    def _update(self, request, partial):
        customer_id = request.data.get("id")

        if not customer_id:
            return JsonResponse({"error": "ID was never Provided"}, status=400)

        try:
            customer = Customers.objects.get(id=customer_id)
            serializer = CustomerSerializer(customer, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"Message": "Success"})
            return JsonResponse(serializer.errors, status=400)
        except Customers.DoesNotExist:
            return JsonResponse({"Message": "User doesn't exist"}, status=404)
