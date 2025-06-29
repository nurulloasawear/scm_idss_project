from django.db import models
import uuid


class AuditLog(models.Model):
   
    class ActionType(models.TextChoices):
        CREATE = 'CREATE', 'Yaratish'
        UPDATE = 'UPDATE', 'Yangilash'
        DELETE = 'DELETE', 'O''chirish'
        LOGIN = 'LOGIN', 'Tizimga kirish'
        EXECUTE = 'EXECUTE', 'Bajarish' # Masalan, hisobot generatsiyasi

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    actor_id = models.CharField(max_length=255, help_text="ID of the user who performed the action")
    action_type = models.CharField(max_length=50, choices=ActionType.choices)
    
    target_model = models.CharField(max_length=100, null=True, blank=True)
    target_id = models.CharField(max_length=255, null=True, blank=True)
    
    details = models.JSONField(default=dict, help_text="e.g., {'old_status': 'pending', 'new_status': 'shipped'}")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.actor_id} performed {self.action_type} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-timestamp']
