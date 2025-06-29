 
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAdminUser
from inventory.models import locations
from .serializers import PublicLocationSerializer,AdminLocationSerializer

class PublicLocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = locations.objects.all().order_by('name')
    serializer_class = PublicLocationSerializer
    permission_classes = [AllowAny]

class AdminLocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = locations.objects.all().order_by('name')
    serializer_class = PublicLocationSerializer
    permission_classes = [IsAdminUser]
