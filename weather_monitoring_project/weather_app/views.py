# weather_app/views.py

from django.shortcuts import render

def weather_view(request):
    # Your logic to handle the request
    return render(request, 'weather_app/weather.html')  # Update with your actual template path

# views.py
from django.shortcuts import render
import pandas as pd
from .visualization import plot_temperature_trends, plot_forecast_trends, plot_combined_summary


def show_visualizations(request):
    # Sample DataFrame creation (replace this with your actual data)
    daily_summary = pd.DataFrame({
        'city': ['City1', 'City1', 'City2', 'City2'],
        'date': ['2023-10-01', '2023-10-02', '2023-10-01', '2023-10-02'],
        'avg_temp': [25, 26, 23, 24],
        'avg_humidity': [60, 65, 55, 58],
        'avg_wind_speed': [5, 4, 6, 5],
    })

    forecast_data = pd.DataFrame({
        'city': ['City1', 'City1', 'City2', 'City2'],
        'forecast_time': ['2023-10-03', '2023-10-04', '2023-10-03', '2023-10-04'],
        'temperature': [27, 28, 25, 26],
        'humidity': [62, 63, 57, 56],
        'wind_speed': [7, 6, 5, 5],
    })

    # Call your plotting functions
    plot_temperature_trends(daily_summary)
    plot_forecast_trends(forecast_data)
    plot_combined_summary(daily_summary, forecast_data)

    # Pass the context to the template
    context = {
        'images': [
            'weather_app/static/images/City1_daily_trends.png',
            'weather_app/static/images/City1_temperature_forecast.png',
            'weather_app/static/images/City1_humidity_forecast.png',
            'weather_app/static/images/City1_wind_speed_forecast.png',
            'weather_app/static/images/City1_combined_summary.png',
            # Add other images as needed
        ]
    }

    return render(request, 'visualizations.html', context)
