from django.contrib import admin
from .models import Farmer, SoilNutrient

# Register Farmer model
@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')  # Fields to display in the list view
    search_fields = ('email', 'name')  # Enable search by these fields


# Register SoilNutrient model
@admin.register(SoilNutrient)
class SoilNutrientAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'nitrogen', 'phosphorus', 'potassium', 'ph')  # Fields to display
    search_fields = ('farmer__email',)  # Search by farmer's email
    list_filter = ('farmer',)  # Add filter options
