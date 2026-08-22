import requests

app_id = 'app_acd7ed1e6c9a46729df8fb92'
app_key = 'nix_live_Wx1RT7ifyPzE5Cw3fkRUTE5T1bOeVqvW'


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
print(response.json())
