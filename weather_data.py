import requests

api_key = 'e01243dd8caff17dfbe23f97ee9a3fba'  # Replace 'YOUR_API_KEY_HERE' with your actual API key

def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        condition = data['weather'][0]['main']
        timestamp = data['dt']
        return city, temp, feels_like, humidity, wind_speed, condition, timestamp
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None


def fetch_weather_forecast(city, api_key):
    try:
        response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}")
        response.raise_for_status()
        forecast_data = response.json()
        return forecast_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None
