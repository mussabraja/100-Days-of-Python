# Day 35 — Weather Forecast API with Umbrella Alert (OpenWeatherMap)

Checks whether it will rain in the next 12 hours at a given location and, if so,
prints **"Bring an Umbrella"**. Built on the OpenWeatherMap **5-day / 3-hour
forecast** API.

Part of my [100 Days of Python](https://github.com/mussabraja/100-Days-of-Python) journey (Angela Yu bootcamp).

## What it does

- Calls the OpenWeatherMap `5 day / 3 hour forecast` endpoint using latitude / longitude.
- Requests only the next **4 forecasts** (`cnt=4`) — 4 × 3-hour windows = the next 12 hours.
- Parses the nested JSON to read each forecast's weather condition `id`.
- Uses a flag to detect if **any** of those windows shows rain, snow, or a storm (condition `id < 700`), and prints an umbrella alert if so.

## Concepts practised

- **API integration** with `requests` — `GET` requests, query parameters, HTTP status handling (`raise_for_status()`).
- **Nested JSON parsing** — walking objects `{}` (by key) and arrays `[]` (by index): `data["list"][i]["weather"][0]["id"]`.
- **Flag pattern** — scan a collection, flip a boolean once a condition is met, then decide once after the loop.
- **Environment variables** — the API key is read from the OS, never hard-coded.

## How the rain check works

The OpenWeatherMap condition `id` describes the weather. Anything **below 700**
means precipitation:

| id range | condition |
|----------|-----------|
| 2xx | Thunderstorm |
| 3xx | Drizzle |
| 5xx | Rain |
| 6xx | Snow |
| 7xx | Atmosphere (mist, fog) |
| 800 | Clear |
| 80x | Clouds |

So the alert fires if any forecast in the next 12 hours has `id < 700`.

## Setup

1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).
2. Store it as an environment variable named `OWM_API_KEY` (do **not** hard-code it):
   - **Windows:** System Environment Variables -> User variables -> New ->
     Name `OWM_API_KEY`, Value = your key (no quotes). Restart your IDE.
   - **macOS / Linux:** add `export OWM_API_KEY="your_key"` to your shell profile.
3. Set your own `lat` / `lng` in `main.py` (get them from [latlong.net](https://www.latlong.net)).
4. Run `main.py`.

## Tech

- Python 3
- `requests`
- OpenWeatherMap API (`data/2.5/forecast`)
