from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .Carrier.views import (
    PublicCarrierViewSet, AdminCarrierViewSet,
)
from .Shipment.views import (
    PublicShipmentViewSet, AdminShipmentViewSet

)
public_router = DefaultRouter()
public_router.register(r'carriers', PublicCarrierViewSet, basename='public-carrier')
public_router.register(r'shipments', PublicShipmentViewSet, basename='public-shipment')

admin_router = DefaultRouter()
admin_router.register(r'carriers', AdminCarrierViewSet, basename='admin-carrier')
admin_router.register(r'shipments', AdminShipmentViewSet, basename='admin-shipment')

urlpatterns = [
    path('public/', include(public_router.urls)),
    path('admin/', include(admin_router.urls)),
]
