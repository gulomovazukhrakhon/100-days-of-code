import requests
from twilio.rest import Client
import os

# Weather
URL = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = YOUR OPENWEATHERMAP API KEY
LAT = YOUR LAT
LON = YOUR LON

# Twilio

ACCOUNT_SID = YOUR TWILIO ACCOUNT SID
AUTH_TOKEN = YOUR TWILIO AUTH TOKEN
VIRTUAL_NUMBER = YOUR VIRTUAL NUMBER
PHONE_NUMBER = YOUR NUMBER

MESSAGE = "It is going to rain. Remember to bring an ☔ "

params = {
    "lat": LAT,
    "lon": LON,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

will_rain = False

response = requests.get(URL, params=params)
data = response.json()
hourly_data = data["hourly"][:12]
id = [hour["weather"][0]["id"] for hour in hourly_data]

for i in id:
    if i > 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
                body=MESSAGE,
                from_=VIRTUAL_NUMBER,
                to=PHONE_NUMBER
    )
    print(message.sid)
