# weather_app/views.py
from django.shortcuts import render,redirect
import requests
from .forms import CityForm
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Feedback

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']  # Update 'username' to 'email'
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)  # Update 'username' to 'email'
        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            return redirect('home')
        else:
            # Handle invalid login
            return render(request, 'weather_app/login.html', {'error': 'Invalid login credentials'})

    return render(request, 'weather_app/login.html')

def signup_view(request):
    if request.method == 'POST':
        new_email = request.POST['new_email']
        new_password = request.POST['new_password']
        # Use create_user to automatically hash the password
        user = User.objects.create_user(username=new_email, password=new_password)
        login(request, user)
        request.session['username'] = user.username# Automatically log in the user after signup
        return redirect('home')

    return render(request, 'weather_app/signup.html')


def logout_view(request):
    logout(request)
    request.session.clear()
    return redirect('login')


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'weather_app/home.html')

def redirect_to_weather_forecast(request):
    return redirect('weather_forecast')

def redirect_to_maps(request):
    return redirect('maps')

def maps(request):
    return render(request, 'weather_app/maps.html')


def weather_forecast(request):
    api_key = '108b3fc52f3399e47ac637e6ec168b01'
    context = {}

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            url = 'https://api.openweathermap.org/data/2.5/weather'
            params = {'q': city, 'appid': api_key, 'units': 'metric'}
            response = requests.get(url, params=params)
            data = response.json()

            context = {'city': city, 'temperature': None, 'forecast': None}

            if 'main' in data:
                context['temperature'] = data['main']['temp']

                # Adding forecast information
                forecast_url = 'https://api.openweathermap.org/data/2.5/forecast'
                forecast_params = {'q': city, 'appid': api_key, 'units': 'metric'}
                forecast_response = requests.get(forecast_url, params=forecast_params)
                forecast_data = forecast_response.json()

                if 'list' in forecast_data:
                    forecast = []
                    for entry in forecast_data['list']:
                        date = entry['dt_txt']
                        temperature = entry['main']['temp']
                        description = entry['weather'][0]['description']
                        forecast.append({'date': date, 'temperature': temperature, 'description': description})

                    context['forecast'] = forecast
        else:
            context['form'] = form

    else:
        form = CityForm()
        context['form'] = form

    return render(request, 'weather_app/weather.html', context)


def feedback(request):
    submitted = False  # Initialize submitted variable

    if request.method == 'POST':
        username = request.POST.get('username')
        feedback_message = request.POST.get('feedback')

        # Save the feedback to the database
        feedback_entry = Feedback(username=username, feedback_message=feedback_message)
        feedback_entry.save()

        # Set a flag to indicate that the form has been submitted
        submitted = True

    return render(request, 'weather_app/feedback.html', {'submitted': submitted})

def privacy_terms(request):
    return render(request, 'weather_app/privacy_terms.html')

def about(request):
    return render(request, 'weather_app/about.html')