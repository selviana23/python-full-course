import requests
city = input("Enter city name:")
url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
response = requests.get(url)
print(response.status_code)
print(response.json())
data = response.json()
print(data)
results = data["results"]
print(results)
location = results[0]

latitude = location["latitude"]
longitude = location["longitude"]

print(latitude)
print(longitude)
weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weather_code"
weather_response = requests.get(weather_url)

weather_data = weather_response.json()
current = weather_data["current"]

temperature = current["temperature_2m"]

print("Temperature:", temperature, "°C")
weather_code = current["weather_code"]

print("Weather code:", weather_code)
if weather_code == 0:
    weather = "Clear sky"
elif weather_code in [1, 2, 3]:
    weather = "Cloudy"
elif weather_code in [61, 63, 65]:
    weather = "Rainy"
else:
    weather = "Other"
print("Weather:", weather)