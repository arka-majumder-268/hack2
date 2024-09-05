from django.db import models

# Create your models here.
# models.py
from django.db import models

class Drug(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

class SupplyOrder(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)
    drug = models.ForeignKey('Drug', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    shipment_date = models.DateField()
    status = models.CharField(max_length=20, choices=[ ('pending', 'Pending'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),])

    def __str__(self):
        return f'Supply Order for {self.drug.name} to {self.hospital.name}'