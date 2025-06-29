from django.db import models
import uuid
class Report(models.Model):
    """
    Tizimda generatsiya qilingan hisobotlar haqidagi ma'lumotlarni saqlaydi.
    """
    class ReportType(models.TextChoices):
        MONTHLY_SALES = 'MONTHLY_SALES', 'Oylik Sotuvlar'
        INVENTORY_TURNOVER = 'INVENTORY_TURNOVER', 'Inventar Aylanmasi'
        SUPPLIER_PERFORMANCE = 'SUPPLIER_PERFORMANCE', 'Yetkazib Beruvchi Samaradorligi'

    class ReportStatus(models.TextChoices):
        PENDING = 'PENDING', 'Kutilmoqda'
        GENERATING = 'GENERATING', 'Yaratilmoqda'
        COMPLETED = 'COMPLETED', 'Yakunlandi'
        FAILED = 'FAILED', 'Xatolik'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    report_type = models.CharField(max_length=100, choices=ReportType.choices)
    status = models.CharField(max_length=50, choices=ReportStatus.choices, default=ReportStatus.PENDING)
    
    requested_by_id = models.CharField(max_length=255)
    
    parameters = models.JSONField(default=dict, help_text="e.g., {'start_date': '2025-01-01', 'end_date': '2025-01-31'}")
    
    file_path = models.FileField(upload_to='reports/', null=True, blank=True)
    
    error_message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.get_report_type_display()} Report ({self.status})"

    class Meta:
        ordering = ['-created_at']
