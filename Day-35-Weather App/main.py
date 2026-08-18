import requests
import os

api_key = os.environ.get("OWM_API_KEY")

lat = 33.001812
lng = 70.067078

api = f"https://api.openweathermap.org/data/2.5/forecast"

parameters ={"lat":lat,
             "lon":lng,
    "appid":api_key,
    "cnt":4,
}

response = requests.get(api,params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for n in data["list"]:
    id_weather = n["weather"][0]["id"]
    if id_weather < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")



