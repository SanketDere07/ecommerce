# your_app_name/urls.py

from django.urls import path
from .views import (
    CustomerListCreateView, CustomerUpdateView,
    ProductListCreateView, ProductCreateView,
    OrderListCreateView, OrderUpdateView, OrderCreateView,
    OrderListByCustomerView, OrderListByProductView,CustomerCreateView
)

urlpatterns = [
    path('api/create/', CustomerCreateView.as_view(), name='customer-create'),
    path('api/customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('api/customers/<int:pk>/', CustomerUpdateView.as_view(), name='customer-update'),

    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/create/', ProductCreateView.as_view(), name='product-create'),
    path('api/orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
    path('api/orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('api/orders/', OrderListByCustomerView.as_view(), name='order-list-by-customer'),
    path('api/orders/', OrderListByProductView.as_view(), name='order-list-by-product'),
]
