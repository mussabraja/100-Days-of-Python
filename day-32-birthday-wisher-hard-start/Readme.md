# Automated Birthday Wisher
A Python script that automatically sends a personalized birthday email when someone's birthday matches today's date.
## What it does
- Reads a list of people (name, email, birth date) from `birthdays.csv`
- Checks whether today's month and day match anyone's birthday
- If there's a match, picks a letter template and inserts the person's name
- Sends the personalized birthday email to that person via Gmail's SMTP server
## How it works
1. **Get today's date** using the `datetime` module (only month and day matter).
2. **Load the birthdays** from `birthdays.csv` into a dictionary keyed by `(month, day)` using `pandas`.
3. **Match** today's date against the dictionary keys.
4. **Personalize** a letter template by replacing the `[NAME]` placeholder with the person's actual name.
5. **Send** the email using `smtplib`.
## Project structure
├── main.py # The main script
├── birthdays.csv # List of people and their birthdays
└── letter_templates/
├── letter_1.txt
├── letter_2.txt
└── letter_3.txt
## Setup
1. Install the required library:
   pip install pandas
2. Add your own entries to `birthdays.csv` in this format:
   name,email,year,month,day
   Ali,ali@example.com,1990,8,13
3. Add your email credentials in `main.py` (see note below).
4. Run the script:
   python main.py
## Note on Gmail
To send email through Gmail you need to:
- Enable 2-Step Verification on your Google account
- Generate an **App Password** and use that in the script (not your normal password)
## Security
Do not commit your real email password or App Password to GitHub. Keep credentials out of the uploaded file, or store them separately.
## Built as part of
Day 32 of the *100 Days of Code: Python* course.
