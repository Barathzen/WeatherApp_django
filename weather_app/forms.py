# weather_app/forms.py
from django import forms

class CityForm(forms.Form):
    city = forms.CharField(label='Enter city', max_length=50)
