import time
from weather_data import fetch_weather_data, fetch_weather_forecast
from data_processing import save_weather_data, save_forecast_data, setup_database, calculate_daily_summary, fetch_all_data
from visualization import plot_temperature_trends, plot_forecast_trends, plot_combined_summary

def main():
    # Step 1: Set up the database
    setup_database()
    
    # Step 2: List of cities to fetch weather data for
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    api_key = 'e01243dd8caff17dfbe23f97ee9a3fba'  # Replace with your actual OpenWeatherMap API key

    # Step 3: Fetch weather data every 5 minutes
    while True:
        for city in cities:
            # Fetch current weather data
            weather_data = fetch_weather_data(city, api_key)
            if weather_data:
                save_weather_data(*weather_data)

            # Fetch forecast data
            forecast_data = fetch_weather_forecast(city, api_key)
            if forecast_data:
                save_forecast_data(city, forecast_data)

        # Step 4: Calculate daily summaries and create plots
        daily_summary = calculate_daily_summary()
        print("Daily Summary:")
        print(daily_summary)

        # Plotting data
        plot_temperature_trends(daily_summary)
        plot_forecast_trends(forecast_data)  # Make sure forecast_data is correctly passed
        plot_combined_summary(daily_summary, forecast_data)  # Ensure forecast_data is available here

        # Step 5: Fetch all stored weather data from the database
        all_data = fetch_all_data()
        print("\nAll Stored Weather Data:")
        for row in all_data:
            print(row)

        # Sleep for 5 minutes before the next update
        time.sleep(300)

if __name__ == "__main__":
    main()
