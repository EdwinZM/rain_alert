import requests
import os
from twilio.rest import Client

API_KEY = "69f04e4613056b159c2761a9d9e664d2"

account_sid = 'ACf6e29020196b55ea4d258849fc7c8302'
auth_token = 'a186aa16794ee9c0a2f8d99eac5a617f'
client = Client(account_sid, auth_token)

params = {
    "lat": 21.161907,
    "lon": -86.851524,
    "appid": API_KEY,
    "exclude": "current,minutely, daily"
}

resp = requests.get(f"https://api.openweathermap.org/data/2.5/onecall", params=params)
resp.raise_for_status()
data = resp.json()
hourly_weather = data["hourly"][:12]

will_rain = False

for i in hourly_weather:
    w_id = i["weather"][0]["id"]
    if w_id < 700:
        will_rain = True

if will_rain:
    message = client.messages \
        .create(
            body="It's going to rain today, bring an umbrella.",
            from_="+18329811002",
            to="+529981613497"
        )
    print(message.status)

 