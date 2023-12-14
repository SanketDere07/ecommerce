# serializers.py

from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Customer, Product, Order, OrderItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def validate_order_date(self, value):
        # Add validation logic to ensure order_date is not in the past
        # ...
     def validate(self, data):
        # Add validation logic for cumulative weight and other constraints
        # ...
        return data
