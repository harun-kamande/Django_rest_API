from django.urls import path
from customer.views import CustomerView

urlpatterns = [
    path('users/', CustomerView.as_view(), name='user-list'),
    path('', CustomerView.as_view(), name='user-list-default'),
    path('customers/', CustomerView.as_view(), name='customer-list-create'),
    path('delete/', CustomerView.as_view(), name='customer-delete'),
    path('update/', CustomerView.as_view(), name='customer-update'),
]
