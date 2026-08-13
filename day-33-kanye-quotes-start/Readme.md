# Kanye Quotes

A desktop app that fetches a random Kanye West quote from an API and displays it on screen at the click of a button.

## What it does

- Shows a background image with a button
- On button click, fetches a random Kanye quote from the Kanye REST API
- Displays the quote on the canvas

## How it works

1. **Send a GET request** to the Kanye REST API using the `requests` library.
2. **Check the response** with `raise_for_status()` to catch any failed requests.
3. **Parse the JSON** response to extract the quote text.
4. **Display the quote** on the Tkinter canvas by updating the text widget with `itemconfig()`.

## Built with

- **Python**
- **requests** — for the API call
- **tkinter** — for the GUI
- **Kanye REST API** — https://api.kanye.rest/

## Setup

1. Install the required library:
   pip install requests
2. Make sure `background.png` and `kanye.png` are in the project folder.
3. Run the script:
   python main.py
## Built as part of

Day 33 of the *100 Days of Code: Python* course.
