from django.db import models


class category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.name
class locations(models.Model):
    class LocationType(models.TextChoices):
        WAREHOUSE = 'WAREHOUSE', 'Warehouse'
        DISTRIBUTION_CENTER = 'DC', 'Distribution Center'
        RETAIL_STORE = 'STORE', 'Retail Store'
    name = models.CharField(max_length=49)
    location_type = models.CharField(max_length=50, choices=LocationType.choices)
    address = models.TextField()
    postal_code = models.CharField(max_length=50)
    storage_capacity_cbm = models.DecimalField(max_digits=12,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class products(models.Model):
    sku = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=80)
    description = models.TextField()
    category = models.ForeignKey('category',on_delete=models.SET_NULL,null=True, blank=True, related_name='products')
    weight_kg = models.DecimalField(max_digits=10,decimal_places=2,null=True, blank=True)
    dimensions = models.JSONField(default=dict, help_text='e.g., {"height_cm": 20, "width_cm": 15}')
    characteristics = models.JSONField(default=dict,help_text='e.g., {"color": "black", "material": "plastic"}')
    lifecycle_status = models.CharField(max_length=50,default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (SKU: {self.sku})"




class inventory(models.Model):
    product = models.ForeignKey('products',on_delete=models.SET_NULL,null=True,blank=True)
    location = models.ForeignKey('locations',on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.PositiveIntegerField()
    safety_stock = models.PositiveIntegerField()
    reorder_point = models.PositiveIntegerField()
    last_updated_at =models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('product', 'location')
        verbose_name_plural = "Inventories"