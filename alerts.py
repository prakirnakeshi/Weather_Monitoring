def check_thresholds(city, temp, threshold_temp=35):
    if temp > threshold_temp:
        print(f"Alert: Temperature in {city} exceeded {threshold_temp}°C!")
