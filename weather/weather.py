import requests

API_KEY = "YOUR_OPENWEATHER_API"

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    data = requests.get(url).json()

    temp = data["main"]["temp"]

    return f"Temperature in {city} is {temp}°C"
