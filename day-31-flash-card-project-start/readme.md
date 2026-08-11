# Day 31 — Flashcard App (French → English)

A desktop flashcard app to learn French vocabulary, built with Python and Tkinter.

## What it does

- Shows a **French** word on the card.
- After **3 seconds**, the card auto-flips to reveal the **English** translation.
- Click **✅** if you know the word — it's removed from the deck and won't appear again.
- Click **❌** if you don't — the word stays in the deck for later.
- Your progress is **saved**: known words are dropped and the remaining words are stored, so the app only ever tests you on what you haven't learned yet. Close and reopen — your progress persists.

## Concepts practised

- **pandas** — reading a CSV into a DataFrame and converting it to a list of records (`read_csv`, `to_dict(orient="records")`)
- **Timed events** — `window.after()` to flip the card, and `window.after_cancel()` to clear stale timers so cards don't flip early
- **File persistence** — saving remaining words to `words_to_learn.csv` with `DataFrame.to_csv(index=False)`
- **Error handling** — `try` / `except FileNotFoundError` to load saved progress if it exists, otherwise fall back to the original word list
- **Tkinter GUI** — Canvas with image and text items, image buttons, grid layout

## How to run

```bash
pip install pandas
python main.py
```

Make sure the `data/` and `images/` folders are in the same directory as `main.py`.

## Project structure

```
day-31-flash-card-project-start/
├── main.py
├── data/
│   ├── french_words.csv
│   └── words_to_learn.csv   (auto-created as you learn)
└── images/
    ├── card_front.png
    ├── card_back.png
    ├── right.png
    └── wrong.png
```

---

Part of my [#100DaysOfCode](https://github.com/mussabraja/100-Days-of-Python) journey — learning Python on the way to Machine Learning.
