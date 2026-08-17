# Day 35 — 5-Day Weather Forecast API (OpenWeatherMap)

Fetches **5-day / 3-hour forecast** data from the OpenWeatherMap API and parses the
nested JSON response to extract the weather condition (`id` and `description`) for
each of the 40 forecast intervals.

Part of my [100 Days of Python](https://github.com/mussabraja/100-Days-of-Python) journey (Angela Yu bootcamp).

## What it does

- Calls the OpenWeatherMap `5 day / 3 hour forecast` endpoint using geographic coordinates (latitude / longitude).
- Passes the query parameters cleanly via a params dictionary (not concatenated onto the URL string).
- Checks the response with `raise_for_status()` so failed requests surface immediately.
- Walks the nested JSON (`list → weather → id / description`) and prints the weather condition for every 3-hour interval across the 5 days.

## Concepts practised

- **API integration** with the `requests` library — `GET` requests, query parameters, HTTP status handling.
- **Nested JSON parsing** — navigating a mix of objects `{}` (accessed by key) and arrays `[]` (accessed by index) layer by layer.
- **Iterating structured data** — looping over the forecast list to process all 40 entries.

## How it works

```
data                        → dict
 └─ "list"                  → array of 40 forecasts
     └─ [each forecast]     → dict
         └─ "weather"       → array
             └─ [0]         → dict
                 └─ "id" / "description"
```

The OpenWeatherMap `id` codes describe the condition (e.g. the 2xx–5xx range covers
thunderstorm, drizzle and rain) — the foundation for the optional rain-alert
extension of this project.

## Tech

- Python 3
- `requests`
- OpenWeatherMap API (`data/2.5/forecast`)

## Note on API keys

The API key (`appid`) is **not** committed to this repo. Get a free key from
[OpenWeatherMap](https://openweathermap.org/api) and add your own before running.
Keep secrets out of version control (e.g. in a `.env` file, git-ignored).
