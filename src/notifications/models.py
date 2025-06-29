from django.db import models
import uuid
class NotificationTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Unique name for the template")
    subject_template = models.CharField(max_length=255, help_text="Subject template, e.g., 'Welcome, {username}!'")
    body_template = models.TextField(help_text="Body template with placeholders, e.g., 'Your order {order_id} has been shipped.'")
    
    class Meta:
        verbose_name = "Notification Template"
        verbose_name_plural = "Notification Templates"

    def __str__(self):
        return self.name

class NotificationLog(models.Model):

    class Channel(models.TextChoices):
        EMAIL = 'EMAIL', 'Elektron Pochta'
        SMS = 'SMS', 'SMS Xabar'
        IN_APP = 'IN_APP', 'Ilova Ichida'

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Kutilmoqda'
        SENT = 'SENT', 'Yuborildi'
        FAILED = 'FAILED', 'Xatolik'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipient = models.CharField(max_length=255)
    channel = models.CharField(max_length=20, choices=Channel.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    template_used = models.ForeignKey(NotificationTemplate, on_delete=models.SET_NULL, null=True, blank=True)
    sent_content = models.TextField()
    error_message = models.TextField(null=True, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To {self.recipient} via {self.channel} ({self.status})"

    class Meta:
        ordering = ['-created_at']


