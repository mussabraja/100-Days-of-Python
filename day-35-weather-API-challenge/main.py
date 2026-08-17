import requests

api_key = "d988986f1a25682518ec132d9d323278"

lat = 33.001812
lng = 70.067078

api = f"https://api.openweathermap.org/data/2.5/forecast"

parameters ={"lat":lat,
             "lon":lng,
    "appid":api_key,
}

response = requests.get(api,params=parameters)
response.raise_for_status()
data = response.json()


for n in data["list"]:
    id_weather = n["weather"][0]["id"]
    description_weather = n["weather"][0]["description"]

    print(id_weather)
    print(description_weather)
