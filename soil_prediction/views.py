from django.shortcuts import render, redirect
from .models import Farmer
from django.contrib.auth.hashers import make_password, check_password


def home(request):
    return render(request, 'home.html')

# Signup view
def farmer_signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        # Check if email already exists
        if Farmer.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Farmer with this Email already exists.'})
        # Create a new farmer
        farmer = Farmer(email=email, name=name, password=make_password(password))
        farmer.save()
        return redirect('farmer_login')
    return render(request, 'signup.html')


# Login view
def farmer_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            farmer = Farmer.objects.get(email=email)
            if check_password(password, farmer.password):  # Verify the password
                # Store the farmer's ID in the session
                request.session['farmer_id'] = farmer.id
                return redirect('soil_form')  # Redirect to the soil form page
            else:
                return render(request, 'login.html', {'error': 'Invalid email or password.'})
        except Farmer.DoesNotExist:
            return render(request, 'login.html', {'error': 'Farmer does not exist. Please sign up first.'})
    return render(request, 'farmer_login.html')


# Protected soil form view
def soil_form(request):
    if 'farmer_id' not in request.session:  # Check if the user is logged in
        return redirect('farmer_login')
    farmer = Farmer.objects.get(id=request.session['farmer_id'])
    return render(request, 'soil_form.html', {'farmer': farmer})
