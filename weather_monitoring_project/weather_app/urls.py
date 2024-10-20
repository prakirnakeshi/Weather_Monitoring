# weather_app/urls.py

from django.urls import path
from .views import weather_view

urlpatterns = [
    # path('weather/', weather_view, name='weather_view'),
    # path('', weather_view, name='weather'),
    path('', weather_view, name='weather_home'),  
]
