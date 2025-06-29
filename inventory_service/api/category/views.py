from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAdminUser
from inventory.models import category
from .serializers import PubluicCategorySerializer,AdminCategorySerializer

class PublicCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = category.objects.all().order_by('name')
    serializer_class  = PubluicCategorySerializer
    permission_classes = [AllowAny]
class AdminCategoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all().order_by('name')
    serializer_class = AdminCategorySerializer
    permission_classes = [IsAdminUser]
    
