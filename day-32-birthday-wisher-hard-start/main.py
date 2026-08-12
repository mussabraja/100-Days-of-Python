import smtplib
import datetime as dt
import pandas as pd

my_email = "mussabsabir27@gmail.com"
my_password = "qvcaybejdlqcfekz"



now = dt.datetime.now()
week_day = now.date()
month_now = now.month
date = week_day.day

tuple_month_day = (month_now,date)
df = pd.read_csv('birthdays.csv')

tuple_dict = df.set_index(['month', 'day']).to_dict('index')

if tuple_month_day in tuple_dict:
    email = tuple_dict[tuple_month_day]['email']
    name = tuple_dict[tuple_month_day]['name']

    with open("letter_templates/letter_1.txt") as file:
        content = file.read()
        new_content = content.replace('[NAME]', name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs=email,msg=f"Subject:Hello\n\n{new_content}")


