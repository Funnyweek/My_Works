import requests
from config import OPEN_WEATHER_MAP_API_KEY
from pprint import pprint
from datetime import datetime
import time

a = "Алматы", "Бишкек", "Ташкент", "Шымкент", "Баку", "Париж", "Сеул"
b = {
        
}
for city_name in a:

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPEN_WEATHER_MAP_API_KEY}&lang=ru&units=metric"

    data = requests.get(url)

    print(data.status_code)
    pprint(data.json())
    data = data.json()
    print(f"Город {data['name']}")
    print(f"Время {datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{data["main"]["temp"]}")
    b[data["name"]] = data["main"]["temp"]
print(b)
print(min(b))
print(max(b))