from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from core.models import AuditLog
from .serializers import AuditLogSerializer

class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    """Adminlar uchun tizimdagi harakatlar jurnalini ko'rish uchun endpoint."""
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAdminUser]
