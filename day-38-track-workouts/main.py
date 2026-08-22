import requests
from datetime import datetime

app_id = 'your app id'
app_key = 'your app key'


url = 'https://app.100daysofpython.dev'


url_post = f'{url}/v1/nutrition/natural/exercise'

header = {
'x-app-id': app_id,
'x-app-key': app_key
}

user_params =   {
  "query": "ran 3 miles",
  "weight_kg": 70,
}
response = requests.post(url = url_post, json=user_params, headers=header)
data = response.json()
user_in = data['exercises'][0]['name']
dur_min = data['exercises'][0]['duration_min']
nf_cal = data['exercises'][0]['nf_calories']


url_sheety = 'YOUR_SHEETY_ENDPOINT'

time_now = datetime.now()
date_n = time_now.strftime("%d/%m/%Y")
time_n = time_now.strftime('%H:%M:%S')


body = {
  'workout': {"date": date_n,
        "time": time_n,
        "exercise": user_in,
        "duration": dur_min,
        "calories": nf_cal,
  }
}

response_sheety = requests.post(
    url=url_sheety,
    json=body,
    auth=("id", "password")
)
print(response_sheety.status_code)
print(response_sheety.text)
