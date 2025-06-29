from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import AuthenticationFailed
from orders.models import Customer_orders as CustomerOrder
# Endi faqat bitta asosiy serializator bor
from .serializers import CustomerOrderSerializer

class UserOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.prefetch_related('items').all().order_by('-order_date')
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerOrderSerializer

   
class AdminCustomerOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.prefetch_related('items').all().order_by('-order_date')
    serializer_class = CustomerOrderSerializer
    permission_classes = [IsAdminUser]
