from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .user.views import (
    UserRegistrationAPIView,
    UserLoginAPIView,
    UserProfileAPIView,
    AdminUserViewSet
)

admin_router = DefaultRouter()
admin_router.register(r'users', AdminUserViewSet, basename='admin-user')

urlpatterns = [
    path('auth/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('auth/login/', UserLoginAPIView.as_view(), name='token_obtain_pair'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me/', UserProfileAPIView.as_view(), name='user-profile'),
    
    path('admin/', include(admin_router.urls)),
]
