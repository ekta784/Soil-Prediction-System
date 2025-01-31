from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.farmer_login, name='farmer_login'),
    path('soil-form/', views.soil_form, name='soil_form'),
    path('signup/', views.farmer_signup, name='farmer_signup'),
]
