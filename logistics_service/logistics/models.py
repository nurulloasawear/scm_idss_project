from django.db import models

class Carrier(models.Model):
    
    class ServiceType(models.TextChoices):
        GROUND = 'GROUND', 'Yer orqali'
        AIR = 'AIR', 'Havo orqali'
        SEA = 'SEA', 'Dengiz orqali'
        RAIL = 'RAIL', 'Temir yo\'l orqali'

    name = models.CharField(max_length=255, unique=True)
    
    service_type = models.CharField(max_length=50, choices=ServiceType.choices)
    
    tracking_url_template = models.URLField(
        max_length=512, 
        blank=True, 
        help_text="e.g., https://carrier.com/track?id={tracking_number}"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Carriers"

class Shipment(models.Model):

    class ShipmentStatus(models.TextChoices):
        LABEL_CREATED = 'LABEL_CREATED', 'Label Yaratildi'
        IN_TRANSIT = 'IN_TRANSIT', 'Yo\'lda'
        OUT_FOR_DELIVERY = 'OUT_FOR_DELIVERY', 'Yetkazish uchun chiqdi'
        DELIVERED = 'DELIVERED', 'Yetkazib Berildi'
        FAILED_ATTEMPT = 'FAILED_ATTEMPT', 'Muvaffaqiyatsiz Urinish'
        EXCEPTION = 'EXCEPTION', 'Istisno Holat'

    customer_order_id = models.UUIDField(help_text="ID of the order from Order Service")
    
    carrier = models.ForeignKey(Carrier, on_delete=models.SET_NULL, null=True, blank=True, related_name='shipments')
    
    tracking_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    
    status = models.CharField(
        max_length=50, 
        choices=ShipmentStatus.choices, 
        default=ShipmentStatus.LABEL_CREATED
    )
    
    dispatched_at = models.DateTimeField(null=True, blank=True)
    estimated_delivery_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Shipment for Order {self.customer_order_id} (Tracking: {self.tracking_number or 'N/A'})"

