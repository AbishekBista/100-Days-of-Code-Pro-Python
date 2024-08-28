import datetime as dt
import random
import smtplib
import pandas
from secret import my_email, password
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# Done

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month=now.month
day=now.day
match_found = False

birthday_data = pandas.read_csv('birthdays.csv')

for (key, value) in birthday_data.iterrows():
    if value["day"] == day and value["month"] == month:
        to_addrs = value["email"]
        receiver = value["name"]
        match_found = True

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if match_found:
    print("Match found")
    # pick a random template
    template_number = random.choice([1, 2, 3])
    print(template_number)
    with open(f"letter_templates/letter_{template_number}.txt", "r") as letter:
        letter_content = letter.read()
        new_letter = letter_content.replace("[NAME]", receiver)
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Happy Birthday!\n\n{new_letter}")
else:
    print("No match found")
# 4. Send the letter generated in step 3 to that person's email address.





