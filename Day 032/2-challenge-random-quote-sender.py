import smtplib
import datetime as dt
import random
from secret import my_email, password

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:

    with open('Birthday Wisher (Day 32) start/quotes.txt') as file:
        quotes = file.read().split('\n')
        random_quote = random.choice(quotes)
        print(random_quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Quote of the Day\n\n{random_quote}")
else:
    print("Waiting for the day to come")

    

