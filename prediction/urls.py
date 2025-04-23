from django.urls import path
from prediction import views  # Import views correctly

urlpatterns = [
    path('', views.indexPage, name='index'),
    path('prediction', views.predictionPage, name='prediction'),
    path("predict/", views.predict_soil_quality, name="predict_soil_quality"),  # Fix reference
]
