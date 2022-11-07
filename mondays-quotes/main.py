import datetime as dt
import random
import smtplib
import os

mail = Receiver Mail
my_password = Sender Password
my_email = Sender Mail

now = dt.datetime.now()
week_day = now.weekday()
quotes = []
if week_day == 5:
    with open("quotes.txt") as data_file:
        data = data_file.readlines()
        for quote in data:
            quotes.append(quote)

    random_quote = random.choice(quotes)
    print(random_quote)

    with smtplib.SMTP_SSL("smtp.mail.yahoo.com", port=465) as connection:
        # connection.start()

        connection.login(
            user=my_email,
            password=my_password
        )

        connection.sendmail(
            from_addr=my_email,
            to_addrs=mail,
            msg=f"Subject:Monday Motivational Quote\n\n"
                f"{random_quote}"
        )
