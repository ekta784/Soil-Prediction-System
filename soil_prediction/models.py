from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom user model for Farmers
class Farmer(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128,default='defaultpassword')  # To store hashed passwords

    def __str__(self):
        return self.email


# Model to store soil nutrient data for each farmer
class SoilNutrient(models.Model):
    farmer = models.OneToOneField(Farmer, on_delete=models.CASCADE, related_name="soil_data")
    nitrogen = models.FloatField(null=True, blank=True)
    phosphorus = models.FloatField(null=True, blank=True)
    potassium = models.FloatField(null=True, blank=True)
    ph = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Soil Data for {self.farmer.email}"
