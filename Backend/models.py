from django.db import models

# Create your models here.
class Vehicle_details(models.Model):
  VEHICLE_TYPES = [
        ('Two', 'Two Wheeler'),
        ('Three', 'Three Wheeler'),
        ('Four', 'Four Wheeler'),
    ]
  vehicle_number=models.CharField(max_length=10,unique=True)
  vehicle_type=models.CharField(max_length=100,choices=VEHICLE_TYPES)
  vehicle_model = models.CharField(max_length=100)
  vehicle_description = models.TextField(null=True)
        
