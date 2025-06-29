from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from logistics.models import Carrier, Shipment
from .serializers import (
    PublicCarrierSerializer, AdminCarrierSerializer,
)

class PublicCarrierViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Carrier.objects.all()
    serializer_class = PublicCarrierSerializer
    permission_classes = [AllowAny]

class AdminCarrierViewSet(viewsets.ModelViewSet):
    queryset = Carrier.objects.all()
    serializer_class = AdminCarrierSerializer
    permission_classes = [IsAdminUser]


