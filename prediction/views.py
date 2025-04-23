import numpy as np
import tensorflow as tf
import joblib
from django.http import JsonResponse
from django.shortcuts import render
import random

# Load trained model
model = tf.keras.models.load_model("soil_quality_model.keras")

# Load scaler
scaler = joblib.load("soil_scaler.pkl")

# Class labels
class_labels = ['Excellent', 'Fair', 'Good', 'Moderate', 'Poor']


def nutrient_recommendation(inputs):
    recommendations = []

    # pH (H2O) recommendation
    ph = inputs['pH_H2O']
    if ph < 5.5:
        recommendations.append(random.choice([
            "Soil is strongly acidic. Apply agricultural lime.",
            "Increase soil pH with dolomitic lime or wood ash."
        ]))
    elif ph > 8:
        recommendations.append(random.choice([
            "Soil is alkaline. Add elemental sulfur or peat moss.",
            "Reduce pH with ammonium-based fertilizers or iron sulfate."
        ]))

    # Nitrogen (N)
    if inputs['N'] < 1.3:
        recommendations.append(random.choice([
            "Nitrogen deficient. Use urea or ammonium nitrate.",
            "Apply organic compost high in nitrogen like manure."
        ]))
    elif inputs['N'] > 4.5:
        recommendations.append("High Nitrogen. Avoid over-fertilizing to prevent leaching.")

    # Phosphorus (P)
    if inputs['P'] < 10:
        recommendations.append(random.choice([
            "Low phosphorus. Use Single Super Phosphate (SSP) or rock phosphate.",
            "Apply Di-Ammonium Phosphate (DAP) for better root development."
        ]))
    elif inputs['P'] > 50:
        recommendations.append("Phosphorus is excessive. Reduce phosphate fertilizers.")

    # Potassium (K)
    if inputs['K'] < 100:
        recommendations.append(random.choice([
            "Potassium low. Apply MOP or wood ash.",
            "Use Sulfate of Potash (SOP) for crops sensitive to chloride."
        ]))
    else:
        pass

    # Organic Carbon (OC)
    if inputs['OC'] < 0.5:
        recommendations.append(random.choice([
            "Add compost or farmyard manure to improve organic matter.",
            "Incorporate green manure or cover crops to build OC."
        ]))
    else:
        pass

    return recommendations


def predict_soil_quality(request):
    if request.method == "POST":
        try:
            # Extract input data from form
            input_data = {
                "pH_CaCl2": float(request.POST['ph_cacl2']),
                "pH_H2O": float(request.POST['ph_h2o']),
                "EC": float(request.POST['ec']),
                "OC": float(request.POST['oc']),
                "CaCO3": float(request.POST['caco3']),
                "P": float(request.POST['p']),
                "N": float(request.POST['n']),
                "K": float(request.POST['k']),
                "Ox_Al": float(request.POST['ox_al']),
                "Ox_Fe": float(request.POST['ox_fe'])
            }

            # Reshape and scale input
            input_array = np.array([list(input_data.values())])
            scaled_input = scaler.transform(input_array)

            # Make prediction
            prediction = model.predict(scaled_input)
            predicted_class = class_labels[np.argmax(prediction)]

            # Get recommendations
            recommendations = nutrient_recommendation(input_data)

            # Return data as JSON
            return JsonResponse({
                'result': predicted_class,
                'features': list(input_data.keys()),
                'values': list(input_data.values()),
                'fertilizer_recommendations': recommendations
            })

        except Exception as e:
            print("Error during prediction:", e)
            return JsonResponse({'error': 'Invalid input data or prediction error.'})

    return render(request, 'prediction.html')

def indexPage(request):
    return render(request, 'index.html')

def predictionPage(request):
    return render(request, 'prediction.html')
