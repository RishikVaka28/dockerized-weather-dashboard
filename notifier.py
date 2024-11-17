import time
import requests
import os
from smtplib import SMTP

API_KEY = os.getenv('WEATHER_API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

def check_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if data.get('main') and data['main']['temp'] > 40:
        send_alert(f"Extreme heat alert in {city}: {data['main']['temp']} °C")

def send_alert(message):
    with SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL, PASSWORD)
        smtp.sendmail(EMAIL, EMAIL, f"Subject: Weather Alert\n\n{message}")

if __name__ == "__main__":
    while True:
        check_weather('London')
        time.sleep(3600)
