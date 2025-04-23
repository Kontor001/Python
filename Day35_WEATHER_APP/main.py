import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "4928a640151c85a73adf42448e04976d"
account_sid = "ACa4c05b9a4e2372c3a433b475f449ce78"
auth_token = "0d498a85630a3f1d4c1f28fb54322f62"

weather_params = {
    "lat": 5.958650,
    "lon": 10.147510,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) <700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    print('client initialized@')
    message = client.messages.create(
        body = "It's going to rain today, Remember to bring an Umbrella ☔",
        from_ ="+12408686408",
        to="+2349060515456"
    )
    print(message.status)
    print(message.date_sent)