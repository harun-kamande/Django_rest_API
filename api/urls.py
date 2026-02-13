from django.urls import path
from customer.views import CustomerView
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path
    path('users/', CustomerView.as_view(), name='user-list'),
    path('', CustomerView.as_view(), name='user-list-default'),
    path('customers/', CustomerView.as_view(), name='customer-list-create'),
    path('delete/', CustomerView.as_view(), name='customer-delete'),
    path('update/', CustomerView.as_view(), name='customer-update'),
]
