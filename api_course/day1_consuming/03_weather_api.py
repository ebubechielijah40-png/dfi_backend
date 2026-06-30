"""
Lesson 3: Real-World API - Open-Meteo Weather (No API Key Needed)
"""

import requests

# === 3.1 Weather Forecast ===
print("=== 3.1 Current Weather ===")
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 6.5244,      # Accra, Ghana
    "longitude": -0.2111,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "auto"
}

resp = requests.get(url, params=params, timeout=10)
if resp.ok:
    data = resp.json()
    current = data["current"]
    print(f"Temperature: {current['temperature_2m']}°C")
    print(f"Humidity: {current['relative_humidity_2m']}%")
    print(f"Wind Speed: {current['wind_speed_10m']} km/h")
else:
    print(f"Error: {resp.status_code}")
print()

# === 3.2 7-Day Forecast ===
print("=== 3.2 7-Day Forecast ===")
params = {
    "latitude": 6.5244,
    "longitude": -0.2111,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "auto",
    "forecast_days": 7
}

resp = requests.get(url, params=params, timeout=10)
if resp.ok:
    data = resp.json()
    daily = data["daily"]
    print(f"{'Date':<12} {'Max°C':<8} {'Min°C':<8} {'Rain mm':<8}")
    print("-" * 36)
    for i in range(len(daily["time"])):
        print(f"{daily['time'][i]:<12} {daily['temperature_2m_max'][i]:<8} "
              f"{daily['temperature_2m_min'][i]:<8} {daily['precipitation_sum'][i]:<8}")
