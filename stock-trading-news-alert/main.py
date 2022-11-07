# IMPORTS
import requests
import datetime as dt
from datetime import timedelta
from twilio.rest import Client


# DATETIME
now = dt.datetime.now()
TODAY = now.date()
YESTERDAY = TODAY - timedelta(days=2)
BEFORE_YESTERDAY = TODAY - timedelta(days=3)


# STOCK PRICE
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_PRICE_API_KEY = STOCK PRICE API KEY

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_PRICE_API_KEY,
}


# NEWS
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = YOUR NEWS API KEY

news_params = {
    "q": STOCK_NAME,
    "from": "2022-07-14",
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}


# Twilio
ACCOUNT_SID = YOUR ACCOUNT SID
AUTH_TOKEN = YOUR AUTH TOKEN
VIRTUAL_NUMBER = YOUR VIRTUAL NUMBER
PHONE_NUMBER = YOUR NUMBER


# API RESPONSES
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_data = news_response.json()


# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
daily_prices = [value for key, value in stock_data.items()]
yesterday_price = daily_prices[1][str(YESTERDAY)]["4. close"]


# TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_price = daily_prices[1][str(BEFORE_YESTERDAY)]["4. close"]


# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
difference = round(abs(float(yesterday_price) - float(before_yesterday_price)), 2)


# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before
#  yesterday.
percentage = round(100 / float(yesterday_price) * difference, 2)


# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage > 0.1:
    first_three_articles = news_data["articles"][:3]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in first_three_articles:
        title = article["title"]
        brief = article["description"]
        website = article["url"]

        MESSAGE = f"{STOCK_NAME} 📈 {percentage}% \nHeadline: {title}\nBrief: {brief}\nCheck out the website: {website}" \
                  f"\n"

        message = client.messages \
                .create(
                    body=MESSAGE,
                    from_=VIRTUAL_NUMBER,
                    to=PHONE_NUMBER
        )
        print(message.sid)
