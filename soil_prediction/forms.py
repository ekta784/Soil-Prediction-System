from django import forms
from .models import Farmer, SoilNutrient


class FarmerLoginForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['email']


class SoilNutrientForm(forms.ModelForm):
    class Meta:
        model = SoilNutrient
        fields = ['nitrogen', 'phosphorus', 'potassium', 'ph']
