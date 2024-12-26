# weather_app/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('redirect_to_weather_forecast/', views.redirect_to_weather_forecast, name='redirect_to_weather_forecast'),
    path('redirect_to_maps/', views.redirect_to_maps, name='redirect_to_maps'),
    path('maps/', views.maps, name='maps'),
    path('feedback/', views.feedback, name='feedback'),
    path('weather_forecast/', views.weather_forecast, name='weather_forecast'),
    path('privacy_terms/', views.privacy_terms, name='privacy_terms'),
    path('about/', views.about, name='about'),
]