import requests
from datetime import datetime
import time

# --- Pixela credentials ---
USER_NAME = "mussabsraja"
TOKEN = "YOUR_TOKEN"         
GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN,
}

# --- 1. Create user account (ek hi dafa chalana hota hai) ---
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# --- 2. Create a graph ---
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji",
}
graph_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# --- Aaj ki date (Pixela format: yyyyMMdd) ---
today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

# --- 3. POST: add a pixel (create) ---
pixel_data = {
    "date": formatted_date,
    "quantity": "10.5",
}
pixel_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}"
# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# --- 4. PUT: update an existing pixel ---
update_data = {
    "quantity": "20",
}
update_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{formatted_date}"
# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

# --- 5. DELETE: remove a pixel ---
delete_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{formatted_date}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
