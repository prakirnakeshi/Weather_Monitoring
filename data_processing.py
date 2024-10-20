import sqlite3
from datetime import datetime
import pandas as pd

def kelvin_to_celsius(temp_kelvin):
    """Convert temperature from Kelvin to Celsius."""
    return temp_kelvin - 273.15

def setup_database():
    """Set up the SQLite database and create the table for weather data."""
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    # Drop the existing table if it exists
    cursor.execute('DROP TABLE IF EXISTS Weather')
    # Create a new table with the updated schema
    cursor.execute('''
        CREATE TABLE Weather (
            city TEXT,
            temperature REAL,
            feels_like REAL,
            humidity INTEGER,
            wind_speed REAL,
            condition TEXT,
            timestamp INTEGER
        )
    ''')
    conn.commit()
    conn.close()


# def save_weather_data(city, temp, feels_like, humidity, wind_speed, main_condition, timestamp):
#     conn = sqlite3.connect('weather_data.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         INSERT INTO Weather (city, temperature, feels_like, humidity, wind_speed, condition, timestamp)
#         VALUES (?, ?, ?, ?, ?, ?, ?)
#     ''', (city, temp, feels_like, humidity, wind_speed, main_condition, timestamp))
#     conn.commit()
#     conn.close()

def save_weather_data(city, temp, feels_like, humidity, wind_speed, condition, timestamp):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Weather
                      (city TEXT, temperature REAL, feels_like REAL, humidity INTEGER, 
                       wind_speed REAL, condition TEXT, timestamp INTEGER)''')
    # Insert all values into the table
    cursor.execute('''INSERT INTO Weather (city, temperature, feels_like, humidity, 
                                           wind_speed, condition, timestamp) 
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (city, temp, feels_like, humidity, wind_speed, condition, timestamp))
    conn.commit()
    conn.close()



def calculate_daily_summary():
    """Calculate daily aggregates for weather data and return as a DataFrame."""
    conn = sqlite3.connect('weather_data.db')
    # Load data into a pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM Weather", conn)
    conn.close()
    
    # Convert the timestamp to a date
    df['date'] = pd.to_datetime(df['timestamp'], unit='s').dt.date
    
    # Define a list of all cities to ensure no city is missing
    all_cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    cities_df = pd.DataFrame({'city': all_cities})
    
    # Group by city and date to calculate the daily aggregates
    daily_summary = df.groupby(['city', 'date']).agg(
        avg_temp=('temperature', 'mean'),
        max_temp=('temperature', 'max'),
        min_temp=('temperature', 'min'),
        avg_feels_like=('feels_like', 'mean'),
        current_temp=('temperature', 'last'),  # Latest temperature of the day
        latest_dt=('timestamp', 'last'),       # Most recent timestamp of the day
        avg_humidity=('humidity', 'mean'),     # Average humidity of the day
        avg_wind_speed=('wind_speed', 'mean'), # Average wind speed of the day
        dominant_condition=('condition', lambda x: x.mode()[0] if not x.mode().empty else None)
    ).reset_index()
    
    # Merge with the cities dataframe to ensure all cities are included
    daily_summary = cities_df.merge(daily_summary, on='city', how='left')
    
    # Fill any missing values with appropriate defaults (e.g., NaN or 0)
    daily_summary['avg_temp'].fillna(0, inplace=True)
    daily_summary['max_temp'].fillna(0, inplace=True)
    daily_summary['min_temp'].fillna(0, inplace=True)
    daily_summary['avg_feels_like'].fillna(0, inplace=True)
    daily_summary['current_temp'].fillna(0, inplace=True)
    daily_summary['latest_dt'].fillna(0, inplace=True)
    daily_summary['avg_humidity'].fillna(0, inplace=True)
    daily_summary['avg_wind_speed'].fillna(0, inplace=True)
    daily_summary['dominant_condition'].fillna('Unknown', inplace=True)
    
    return daily_summary

def fetch_all_data():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    # Fetch all columns from the Weather table
    cursor.execute('SELECT city, temperature, feels_like, humidity, wind_speed, condition, timestamp FROM Weather')
    rows = cursor.fetchall()
    conn.close()
    return rows

# def save_forecast_data(city, forecast_data):
#     conn = sqlite3.connect('weather_data.db')
#     cursor = conn.cursor()
#     # Create the table if it doesn't exist
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS WeatherForecast (
#             city TEXT,
#             forecast_time INTEGER,
#             temperature REAL,
#             humidity INTEGER,
#             wind_speed REAL,
#             condition TEXT
#         )
#     ''')
#     # Insert the forecast data
#     for entry in forecast_data['list']:
#         forecast_time = entry['dt']
#         temp = kelvin_to_celsius(entry['main']['temp'])
#         humidity = entry['main']['humidity']
#         wind_speed = entry['wind']['speed']
#         condition = entry['weather'][0]['main']
#         cursor.execute('''
#             INSERT INTO WeatherForecast (city, forecast_time, temperature, humidity, wind_speed, condition)
#             VALUES (?, ?, ?, ?, ?, ?)
#         ''', (city, forecast_time, temp, humidity, wind_speed, condition))
#     conn.commit()
#     conn.close()


def save_forecast_data(city, forecast_data):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    # Create the Forecast table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Forecast (
            city TEXT,
            forecast_time INTEGER,
            temperature REAL,
            feels_like REAL,
            humidity INTEGER,
            wind_speed REAL,
            condition TEXT
        )
    ''')
    # Insert forecast data into the Forecast table
    for entry in forecast_data['list']:
        forecast_time = entry['dt']
        temp = kelvin_to_celsius(entry['main']['temp'])
        feels_like = kelvin_to_celsius(entry['main']['feels_like'])
        humidity = entry['main']['humidity']
        wind_speed = entry['wind']['speed']
        condition = entry['weather'][0]['main']
        cursor.execute('''
            INSERT INTO Forecast (city, forecast_time, temperature, feels_like, humidity, wind_speed, condition)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (city, forecast_time, temp, feels_like, humidity, wind_speed, condition))
    conn.commit()
    conn.close()
