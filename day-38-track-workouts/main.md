# Day 38 - Workout Tracking (Nutritionix + Sheety API)

A Python app that logs workouts to a Google Sheet using natural language.
Type what you did in plain English (e.g. "ran 3 miles and swam for 30 minutes"),
and the app parses it into structured exercise data and saves it as a new row.

## How it works

1. **Nutritionix API** — takes a natural-language exercise description and returns
   structured data (exercise name, duration, calories burned) based on user body stats.
2. **Sheety API** — writes that data as a new row into a connected Google Sheet,
   with the current date and time added via Python's `datetime` module.

## Concepts practised

- Chaining two APIs (one API's output feeds the next API's input)
- POST requests with header-based auth (`x-app-id` / `x-app-key`) for Nutritionix
- HTTP Basic Authentication for Sheety (via `requests` `auth=` parameter)
- Nested JSON request bodies (`{"workout": {...}}`)
- Parsing nested JSON responses to extract specific values
- Formatting dates/times with `strftime`

## Tech

- Python
- `requests`
- `datetime`

## Setup

Replace the placeholders in the code with your own credentials:

- `app_id` / `app_key` — from your Nutritionix account
- `url_sheety` — your Sheety project endpoint
-
