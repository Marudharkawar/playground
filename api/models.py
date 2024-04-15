from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('physical', 'Physical'),
        ('digital', 'Digital'),
    ]

    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    manufacturer = models.CharField(max_length=100, null=False)
    serial_number = models.CharField(max_length=100, unique=True, null=False)
    manufacture_date = models.DateField(null=False)
    warranty_information = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='physical', null=False)
    created_by = models.ForeignKey(User, related_name='products_created', on_delete=models.SET_NULL, null=True, editable=False)
    updated_by = models.ForeignKey(User, related_name='products_updated', on_delete=models.SET_NULL, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
