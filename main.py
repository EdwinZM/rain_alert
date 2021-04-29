import requests
import os
from twilio.rest import Client

API_KEY = os.environ.get('API_KEY')

account_sid=os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
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

 