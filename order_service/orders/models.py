from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Suppliers(models.Model):
    name = models.CharField(max_length=250,unique=True)
    contact_person = models.CharField(max_length=250,blank=True)
    contact_info = models.JSONField(default=dict,help_text='e.g., {"email": "contact@supplier.com", "phone": "+12345"}')
    address = models.TextField(blank=True)
    performance_rating = models.DecimalField(max_digits=3,
                                             decimal_places=2,
                                             null=True,
                                             blank=True,
                                             validators=[MinValueValidator(0.0),MaxValueValidator(5.0)]
                                             )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.name
class Customer_orders(models.Model):
    class Order_st(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        PROCESSING = 'PROCESSING', 'Processing'
        SHIPPED = 'SHIPPED', 'Shipped'
        DELIVERED = 'DELIVERED', 'Delivered'
        CANCELLED = 'CANCELLED', 'Cancelled'

    customer_id = models.PositiveIntegerField(help_text="ID of the user from User Service")
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20,choices=Order_st.choices,default=Order_st.PENDING)
    shipping_address = models.TextField()
    total_amount = models.DecimalField(max_digits=12,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Order_items(models.Model):
    order = models.ForeignKey('Customer_orders',on_delete=models.CASCADE,related_name='items')
    product_id = models.UUIDField(help_text="ID of the product from Inventory Service")
    quantity = models.IntegerField()
    unit_prices = models.DecimalField(max_digits=10,decimal_places=2)