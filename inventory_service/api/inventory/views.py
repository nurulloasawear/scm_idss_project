from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from inventory.models import inventory as Inventory
from .serializers import PublicInventorySerializer, AdminInventorySerializer

class PublicInventoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Jamoat uchun ochiq, faqat inventarni ko'rish uchun (GET)."""
    queryset = Inventory.objects.select_related('product', 'location').all()
    serializer_class = PublicInventorySerializer
    permission_classes = [IsAuthenticated] # Faqat tizimga kirganlar ko'rsin

class AdminInventoryViewSet(viewsets.ModelViewSet):
    """Adminlar uchun inventarni to'liq boshqarish (CRUD)."""
    queryset = Inventory.objects.select_related('product', 'location').all()
    serializer_class = AdminInventorySerializer
    permission_classes = [IsAdminUser]
