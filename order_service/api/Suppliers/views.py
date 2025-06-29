from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from orders.models import Suppliers as Supplier
from .serializers import PublicSupplierSerializer, AdminSupplierSerializer

class PublicSupplierViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Supplier.objects.all().order_by('name')
    serializer_class = PublicSupplierSerializer
    permission_classes = [AllowAny]

class AdminSupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('name')
    serializer_class = AdminSupplierSerializer
    permission_classes = [IsAdminUser]

