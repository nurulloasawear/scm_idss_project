from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .category.views import PublicCategoryViewSet
from .locations.views import PublicLocationViewSet
from .products.views import PublicProductViewSet
from .inventory.views import PublicInventoryViewSet
from .category.views import AdminCategoryViewSet
from .locations.views import AdminLocationViewSet
from .products.views import AdminProductViewSet
from .inventory.views import AdminInventoryViewSet

public_router = DefaultRouter()
public_router.register(r'categories', PublicCategoryViewSet, basename='public-category')
public_router.register(r'locations', PublicLocationViewSet, basename='public-location')
public_router.register(r'products', PublicProductViewSet, basename='public-product')
public_router.register(r'inventory', PublicInventoryViewSet, basename='public-inventory')

admin_router = DefaultRouter()
admin_router.register(r'categories', AdminCategoryViewSet, basename='admin-category')
admin_router.register(r'locations', AdminLocationViewSet, basename='admin-location')
admin_router.register(r'products', AdminProductViewSet, basename='admin-product')
admin_router.register(r'inventory', AdminInventoryViewSet, basename='admin-inventory')

urlpatterns = [
    path('public/', include(public_router.urls)),
    path('admin/', include(admin_router.urls)),
]
