from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from logistics.models import Carrier, Shipment
from .serializers import (
    PublicShipmentSerializer, AdminShipmentSerializer
)
class PublicShipmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = PublicShipmentSerializer
    permission_classes = [IsAuthenticated]

class AdminShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = AdminShipmentSerializer
    permission_classes = [IsAdminUser]