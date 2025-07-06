from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from .forms import DiabetesForm
from .train_model import primary_model, validator_model
import numpy as np # type: ignore
from django.views.decorators.csrf import csrf_exempt
# Custom user model
CustomUser = get_user_model()
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # or home/dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, 'predictor/signup.html', {'form': form})

# 🔐 Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'predictor/login.html', {'form': form})

# 🚪 Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# 🏠 Public homepage
def home(request):
    return render(request, 'predictor/home.html')

# 🧾 Educational diabetes info page
def diabetes_info(request):
    return render(request, 'predictor/diabetes_info.html')

# 💉 Prediction logic – shown on dashboard
@login_required
def dashboard(request):
    result = ""
    if request.method == "POST" or request.session.get('form_data'):
        form_data = request.POST if request.method == "POST" else request.session.pop('form_data', None)
        if form_data:
            form = DiabetesForm(form_data)
            if form.is_valid():
                data = list(form.cleaned_data.values())
                input_data = np.array([data])
                prob1 = primary_model.predict_proba(input_data)[0][1]
                prob2 = validator_model.predict_proba(input_data)[0][1]
                avg_prob = round((prob1 + prob2) / 2, 2)

                if avg_prob > 0.75:
                    result = f"⚠️ High risk of diabetes detected. (Risk Score: {avg_prob * 100:.1f}%)"
                elif avg_prob > 0.5:
                    result = f"⚠️ Moderate risk – monitor health. (Risk Score: {avg_prob * 100:.1f}%)"
                else:
                    result = f"✅ No significant risk of diabetes. (Risk Score: {avg_prob * 100:.1f}%)"
            else:
                result = "Invalid form data."
        else:
            form = DiabetesForm()
    else:
        form = DiabetesForm()

    return render(request, "predictor/dashboard.html", {"form": form, "result": result})

import time

@csrf_exempt # type: ignore
@login_required
def processing_view(request):
    if request.method == 'POST':
        request.session['form_data'] = request.POST  # Store form data in session
        return render(request, 'predictor/processing.html')
    return redirect('dashboard')