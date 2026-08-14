import requests
from datetime import datetime, UTC
import smtplib
import time


my_email = "enter email"
my_password = "enter password"
to_email = "mussab@gmail.com"

MY_LAT = 33.001812  # Your latitude
MY_LONG = 70.067078  # Your longitude


while True:
    time.sleep(60)

    # ISS ki current position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Sunrise / sunset
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(UTC)

    iss_close = MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    is_dark = time_now.hour < sunrise or time_now.hour > sunset

    if iss_close and is_dark:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:Hello\n\nCurrently satellite is above you at {iss_longitude} and {iss_latitude}"
            )
