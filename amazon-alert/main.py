import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

# Amazon
ACCEPT_LANGUAGE = YOUR ACCEPT LANGUAGE
USER_AGENT = YOUR USER AGENT
PRODUCT_URL = "https://www.amazon.com/Anthology-Standard-Compact-Contents-Tracking/dp/B09ZKCRM4D/ref=sr_" \
              "1_3?keywords=bts+proof+album&qid=1660654895&sprefix=bts+%2Caps%2C279&sr=8-3"
BUY_PRICE = 85

# SMTP
sender = SENDER
password = YOUR APP PASSWORD
receiver = RECEIVER

# Amazon
headers = {
    'Accept-Language': ACCEPT_LANGUAGE,
    'User-Agent': USER_AGENT
}

response = requests.get(url=PRODUCT_URL, headers=headers)
contents = response.text

soup = BeautifulSoup(contents, "lxml")
price = int(soup.find(name="span", class_="a-price-whole").getText().replace('.', ''))
title = "BTS Proof Album"

# SMTP
message = f"{title} is now ${price}.99"

if price < BUY_PRICE:
    with smtplib.SMTP_SSL("smtp.mail.yahoo.com", port=465) as connection:

        connection.login(
            user=sender,
            password=password
        )

        connection.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg=f"Subject: Amazon Price Alert!\n\n"
                f"{message}"
        )
