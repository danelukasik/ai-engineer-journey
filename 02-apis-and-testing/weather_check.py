# weather.py
import requests

def get_weather(city_name, lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m,relative_humidity_2m",
        "temperature_unit": "fahrenheit"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None
    current = response.json()["current"]
    return {
        "city": city_name,
        "temp_f": current["temperature_2m"],
        "wind_kmh": current["wind_speed_10m"],
        "humidity_pct": current["relative_humidity_2m"]
    }