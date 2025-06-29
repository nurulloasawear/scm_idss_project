from rest_framework import serializers
from reports.models import Report

class ReportSerializer(serializers.ModelSerializer):
    """Hisobotlarni boshqarish uchun serializator."""
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    report_type_display = serializers.CharField(source='get_report_type_display', read_only=True)

    class Meta:
        model = Report
        fields = [
            'id', 'report_type', 'report_type_display', 'status', 'status_display',
            'parameters', 'file_path', 'error_message', 'created_at', 'completed_at'
        ]
        # Bu maydonlar faqat o'qish uchun, ular avtomatik to'ldiriladi.
        read_only_fields = ['status', 'file_path', 'error_message', 'completed_at']
