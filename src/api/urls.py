from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .core.views import AuditLogViewSet
from .notifictions.views import NotificationTemplateViewSet, NotificationLogViewSet
from .reports.views import ReportViewSet

router = DefaultRouter()
router.register(r'audit-logs', AuditLogViewSet, basename='audit-log')
router.register(r'notification-templates', NotificationTemplateViewSet, basename='notification-template')
router.register(r'notification-logs', NotificationLogViewSet, basename='notification-log')
router.register(r'reports', ReportViewSet, basename='report')

urlpatterns = [

    path('', include(router.urls)),
]