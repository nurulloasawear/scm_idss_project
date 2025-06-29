
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from inventory.models import products as Product
from .serializers import PublicProductSerializer, AdminProductSerializer

class PublicProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.select_related('category').all().order_by('name')
    serializer_class = PublicProductSerializer
    permission_classes = [AllowAny]

class AdminProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all().order_by('name')
    serializer_class = AdminProductSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
