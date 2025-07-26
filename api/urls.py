from django.urls import path
from .views import (
    UserListView,
    CustomerView,
    CustomerDeleteView,
    CustomerUpdateView,
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('', UserListView.as_view(), name='user-list-default'),
    path('customers/', CustomerView.as_view(), name='customer-list-create'),
    path('delete/', CustomerDeleteView.as_view(), name='customer-delete'),
    path('update/', CustomerUpdateView.as_view(), name='customer-update'),
]
