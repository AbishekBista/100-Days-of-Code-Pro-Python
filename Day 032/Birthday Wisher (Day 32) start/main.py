import smtplib
from secret import my_email, password

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="abishek.bista@yahoo.com", msg="Subject:Hello\n\nThis is the body of my email")
