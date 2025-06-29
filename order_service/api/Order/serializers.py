from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from orders.models import Customer_orders as CustomerOrder, Order_items as OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ['order']


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = "__all__"