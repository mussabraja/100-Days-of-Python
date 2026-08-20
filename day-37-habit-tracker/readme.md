# Day 37 — Pixela Habit Tracker (REST API, Full CRUD)

A habit-tracking script that talks to the [Pixela](https://pixe.la/) REST API
to build a GitHub-style pixel graph. Demonstrates all four core HTTP
operations — **POST, PUT, DELETE** — with **header-based authentication**.

Part of my [100 Days of Code](https://github.com/mussabraja/100-Days-of-Python) journey.

## What it does

Tracks a daily habit (here: cycling distance in km) by writing data points
("pixels") to a personal Pixela graph. Each pixel represents one day's value.

## Concepts practised

- **REST API CRUD operations**
  - `POST`   → create a user, create a graph, add a pixel
  - `PUT`    → update an existing pixel's value
  - `DELETE` → remove a pixel
- **Header-based authentication** using an `X-USER-TOKEN` header
  (the same pattern used by most ML/AI APIs, e.g. `Authorization: Bearer <key>`)
- **Request body vs headers** — data goes in the JSON body, identity/auth in headers
- **Dynamic endpoints** built with f-strings
- **Date formatting** with `datetime.strftime("%Y%m%d")` for the API's required format

## Tech

- Python 3
- [`requests`](https://pypi.org/project/requests/) library
- [Pixela API](https://docs.pixe.la/)

## Usage

1. Set your credentials at the top of the file:
```python
   USER_NAME = "your_username"
   TOKEN = "your_token"
   GRAPH_ID = "graph1"
```
2. Uncomment the request you want to run (create account → create graph →
   add/update/delete pixel), one at a time.
3. View your graph at:
   `https://pixe.la/v1/users/<USER_NAME>/graphs/<GRAPH_ID>.html`

## Note

Pixela runs on **UTC**, so a pixel's date may differ from your local date
by a day depending on your timezone.
