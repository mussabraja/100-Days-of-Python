# ISS Overhead Notifier

A Python script that emails you when the International Space Station (ISS) is passing overhead **and** it's dark outside — so you can step out and spot it in the night sky.

## What it does

- Checks the ISS's current position every 60 seconds
- Checks whether it's currently dark at your location
- If the ISS is overhead **and** it's dark, sends you an email telling you to look up

## How it works

1. **Get the ISS position** from the Open Notify API (its current latitude and longitude).
2. **Check if it's close** — whether the ISS is within ±5 degrees of your latitude and longitude.
3. **Get sunrise/sunset times** for your location from the Sunrise-Sunset API (using `formatted=0` for ISO/UTC times).
4. **Check if it's dark** — whether the current hour is before sunrise or after sunset.
5. **Send an email** via `smtplib` if both conditions are true.
6. **Repeat** the whole check every 60 seconds using a `while` loop and `time.sleep(60)`.

## Built with

- **Python**
- **requests** — for the API calls
- **smtplib** — to send the email
- **datetime** — for the current UTC time
- **Open Notify ISS API** — http://api.open-notify.org/iss-now.json
- **Sunrise-Sunset API** — https://api.sunrise-sunset.org

## Setup

1. Install the required library:
   pip install requests
2. 2. Set your own latitude and longitude in `MY_LAT` and `MY_LONG`.
3. Add your email credentials (see security note below).
4. Run the script:
   python main.py

## A note on time zones

Both the sunrise/sunset times and the current time are handled in **UTC** so the comparison is correct. Mixing UTC (from the API) with local time would throw the dark/light check off by your timezone offset.

## Security

Don't commit your real email password (or Gmail App Password) to GitHub. Keep credentials out of the uploaded file, or load them from environment variables.

## Built as part of

Day 33 of the *100 Days of Code: Python* course.
