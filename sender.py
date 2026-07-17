import smtplib
import os
import random

my_email = os.environ.get("my_email")
my_password = os.environ.get("my_password")
recipients = "gulalkaya@hotmail.co.uk"


def send_email():
    with open("./data/quotes.txt", "r") as file:
        quotes = file.readlines()
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipients,
            msg=f"Subject: Daily Quote\n\n{random.choice(quotes)}"
        ) 



send_email()
