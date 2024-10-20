import matplotlib.pyplot as plt
import os

def plot_temperature_trends(daily_summary):
    """
    Plot daily average temperature, humidity, and wind speed trends for each city
    and save the plots as images.
    """
    for city in daily_summary['city'].unique():
        city_data = daily_summary[daily_summary['city'] == city]
        
        plt.figure(figsize=(12, 6))
        
        # Plot average temperature
        plt.plot(city_data['date'], city_data['avg_temp'], label=f'{city} Avg Temp', color='tab:red', marker='o')
        
        # Plot average humidity
        plt.plot(city_data['date'], city_data['avg_humidity'], label=f'{city} Avg Humidity', color='tab:blue', linestyle='--')
        
        # Plot average wind speed
        plt.plot(city_data['date'], city_data['avg_wind_speed'], label=f'{city} Avg Wind Speed', color='tab:green', linestyle=':')
        
        plt.xlabel('Date')
        plt.ylabel('Values')
        plt.title(f'{city} Daily Weather Trends')
        plt.legend()
        plt.grid(True)
        
        # Save the plot as a PNG file
        image_path = os.path.join('weather_app', 'static', 'images', f'{city}_daily_trends.png')
        plt.savefig(image_path)
        plt.close()  # Close the figure to free memory

def plot_forecast_trends(forecast_data):
    """
    Plot the forecasted temperature, humidity, and wind speed trends for each city
    and save the plots as images.
    """
    for city in forecast_data['city'].unique():
        city_forecast = forecast_data[forecast_data['city'] == city]
        
        # Plot temperature trends
        plt.figure(figsize=(10, 5))
        plt.plot(city_forecast['forecast_time'], city_forecast['temperature'], label=f'{city} Temperature', color='tab:red')
        plt.xlabel('Forecast Time')
        plt.ylabel('Temperature (°C)')
        plt.title(f'{city} 5-Day Temperature Forecast')
        plt.legend()
        plt.grid(True)
        
        # Save the plot as a PNG file
        temp_image_path = os.path.join('weather_app', 'static', 'images', f'{city}_temperature_forecast.png')
        plt.savefig(temp_image_path)
        plt.close()
        
        # Plot humidity trends
        plt.figure(figsize=(10, 5))
        plt.plot(city_forecast['forecast_time'], city_forecast['humidity'], label=f'{city} Humidity', color='tab:blue')
        plt.xlabel('Forecast Time')
        plt.ylabel('Humidity (%)')
        plt.title(f'{city} 5-Day Humidity Forecast')
        plt.legend()
        plt.grid(True)
        
        # Save the plot as a PNG file
        humidity_image_path = os.path.join('weather_app', 'static', 'images', f'{city}_humidity_forecast.png')
        plt.savefig(humidity_image_path)
        plt.close()
        
        # Plot wind speed trends
        plt.figure(figsize=(10, 5))
        plt.plot(city_forecast['forecast_time'], city_forecast['wind_speed'], label=f'{city} Wind Speed', color='tab:green')
        plt.xlabel('Forecast Time')
        plt.ylabel('Wind Speed (m/s)')
        plt.title(f'{city} 5-Day Wind Speed Forecast')
        plt.legend()
        plt.grid(True)
        
        # Save the plot as a PNG file
        wind_speed_image_path = os.path.join('weather_app', 'static', 'images', f'{city}_wind_speed_forecast.png')
        plt.savefig(wind_speed_image_path)
        plt.close()

def plot_combined_summary(daily_summary, forecast_data):
    """
    Plot combined trends showing both daily summary and forecast for temperature, humidity, and wind speed
    and save the plots as images.
    """
    for city in daily_summary['city'].unique():
        city_data = daily_summary[daily_summary['city'] == city]
        city_forecast = forecast_data[forecast_data['city'] == city]
        
        plt.figure(figsize=(12, 6))
        
        # Plot daily average temperature
        plt.plot(city_data['date'], city_data['avg_temp'], label=f'{city} Daily Avg Temp', marker='o', color='tab:orange')
        
        # Plot forecasted temperature
        plt.plot(city_forecast['forecast_time'], city_forecast['temperature'], label=f'{city} Forecast Temp', linestyle='--', color='tab:red')
        
        # Plot daily average humidity
        plt.plot(city_data['date'], city_data['avg_humidity'], label=f'{city} Daily Avg Humidity', marker='x', color='tab:blue')
        
        # Plot forecasted humidity
        plt.plot(city_forecast['forecast_time'], city_forecast['humidity'], label=f'{city} Forecast Humidity', linestyle='--', color='tab:cyan')
        
        # Plot daily average wind speed
        plt.plot(city_data['date'], city_data['avg_wind_speed'], label=f'{city} Daily Avg Wind Speed', marker='d', color='tab:green')
        
        # Plot forecasted wind speed
        plt.plot(city_forecast['forecast_time'], city_forecast['wind_speed'], label=f'{city} Forecast Wind Speed', linestyle='--', color='tab:olive')
        
        plt.xlabel('Date / Forecast Time')  
        plt.ylabel('Values')
        plt.title(f'{city} Daily Summary vs 5-Day Forecast')
        plt.legend()
        plt.grid(True)
        
        # Save the plot as a PNG file
        combined_image_path = os.path.join('weather_app', 'static', 'images', f'{city}_combined_summary.png')
        plt.savefig(combined_image_path)
        plt.close()
