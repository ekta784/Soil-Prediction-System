import numpy as np
import tensorflow as tf
import joblib
import json
from django.http import JsonResponse
from django.shortcuts import render

# Load trained model
model = tf.keras.models.load_model("soil_quality_model.keras")

# Load scaler (Make sure you saved this during training using joblib)
scaler = joblib.load("soil_scaler.pkl")

# Class labels (Ensure they match training order)
class_labels = ['Excellent', 'Fair', 'Good', 'Moderate', 'Poor']

def predict_soil_quality(request):
    if request.method == "POST":
        try:
            # Extract input data from form
            input_data = [
                float(request.POST['ph_cacl2']),
                float(request.POST['ph_h2o']),
                float(request.POST['ec']),
                float(request.POST['oc']),
                float(request.POST['caco3']),
                float(request.POST['p']),
                float(request.POST['n']),
                float(request.POST['k']),
                float(request.POST['ox_al']),
                float(request.POST['ox_fe'])
            ]

            feature_names = [
                "pH (CaCl2)", "pH (H2O)", "EC", "OC", "CaCO3",
                "P", "N", "K", "Ox_Al", "Ox_Fe"
            ]

            # Reshape and scale input
            input_array = np.array([input_data])
            scaled_input = scaler.transform(input_array)

            # Make prediction
            prediction = model.predict(scaled_input)
            predicted_class = class_labels[np.argmax(prediction)]

            # Return data as JSON for real-time graph update
            return JsonResponse({
                'result': predicted_class,
                'features': feature_names,
                'values': input_data
            })

        except Exception as e:
            print("Error during prediction:", e)
            return JsonResponse({'error': 'Invalid input data or prediction error.'})

    return render(request, 'prediction.html')


def indexPage(request):
    page_info = 1
    return render(request, 'index.html', {'page_info': page_info})


def predictionPage(request):
    page_info = 2
    return render(request, 'prediction.html', {'page_info': page_info})
