from django.urls import path
from customer.views import CustomerView
from rest_framework.authtoken.views import obtain_auth_token
from product.views import ProductView




from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)   


urlpatterns = [

    path("token/", obtain_auth_token, name="api_token_auth"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', CustomerView.as_view(), name='user-list'),
    path('products/', ProductView.as_view(), name='product-list-create'),
    path('', CustomerView.as_view(), name='user-list-default'),
    path('customers/', CustomerView.as_view(), name='customer-list-create'),
    path('delete/', CustomerView.as_view(), name='customer-delete'),
    path('update/', CustomerView.as_view(), name='customer-update'),
]
