# Quizzler — True/False Quiz App

A desktop quiz game that pulls **live True/False questions** from the internet and runs them through a clean Tkinter GUI. Built as **Day 34** of the *100 Days of Code* Python bootcamp.

## What it does

- Fetches 10 fresh True/False questions from the **Open Trivia Database API** every time you run it — no hardcoded questions.
- Shows one question at a time on a canvas, with **True** and **False** image buttons.
- Gives instant **green / red** colour feedback for each answer.
- Tracks and displays a **live score** that updates as you play.
- Ends cleanly once all questions are done — buttons disable and a "quiz complete" message shows (no crash).

## How it works

The app is built with an object-oriented, multi-file structure:

- **`data.py`** — makes the API request (`requests.get` with a `params` dictionary for `amount` and `type=boolean`) and stores the parsed question list.
- **`question_model.py`** — a `Question` class that models a single question (text + answer).
- **`quiz_brain.py`** — a `QuizBrain` class holding the quiz logic: serving the next question, checking answers, tracking score, and knowing when questions run out.
- **`ui.py`** — a `QuizInterface` class (Tkinter) that displays everything and wires the buttons. It uses **composition** — the `QuizBrain` object is passed in and used via `self.quiz`.
- **`main.py`** — builds the question bank, creates the `QuizBrain`, and hands it to the `QuizInterface`.

## Concepts practised

- Making API `GET` requests with query parameters via a `params` dictionary
- Parsing a JSON response (`response.json()["results"]`)
- Cleaning API text with `html.unescape()`
- Object-oriented design across multiple files (composition, not inheritance)
- Tkinter: `Canvas`, `create_text`, `itemconfig`, image `Button`s, `grid` layout, `window.after()` for timed colour feedback, and disabling widgets with `state="disabled"`

## Tech

- Python 3
- `requests` library
- `tkinter` (standard library)
- [Open Trivia Database API](https://opentdb.com/)

## Run it

```bash
pip install requests
python main.py
```

---

Part of my [100 Days of Code](https://github.com/mussabraja/100-Days-of-Python) journey — EE grad transitioning to ML Engineering.
