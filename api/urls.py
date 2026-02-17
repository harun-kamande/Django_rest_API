from django.urls import path
from customer.views import CustomerView
from rest_framework.authtoken.views import obtain_auth_token
from orders.views import OrdersView
from product.views import ProductView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('users/', CustomerView.as_view(), name='user-list'),
    path("orders/", OrdersView.as_view(), name="orders-list"),
    path("products/", ProductView.as_view(), name="products-list"),
    path('', CustomerView.as_view(), name='user-list-default'),
    path('customers/', CustomerView.as_view(), name='customer-list-create'),
    path('delete/', CustomerView.as_view(), name='customer-delete'),
    path('update/', CustomerView.as_view(), name='customer-update'),
]
