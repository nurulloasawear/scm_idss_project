from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
