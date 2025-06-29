from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .Suppliers.views import PublicSupplierViewSet, AdminSupplierViewSet
from .Order.views import UserOrderViewSet, AdminCustomerOrderViewSet

public_router = DefaultRouter()
public_router.register(r'suppliers', PublicSupplierViewSet, basename='public-supplier')
public_router.register(r'orders', UserOrderViewSet, basename='user-order')

admin_router = DefaultRouter()
admin_router.register(r'suppliers', AdminSupplierViewSet, basename='admin-supplier')
admin_router.register(r'orders', AdminCustomerOrderViewSet, basename='admin-order')

urlpatterns = [
    path('public/', include(public_router.urls)),
    path('admin/', include(admin_router.urls)),
]