"""
Небольшой скрипт для показа текущей погоды через OpenWeatherMap API.

Настройка:
1) Зарегистрируйтесь на https://openweathermap.org/ и получите API-ключ.
2) Экспортируйте ключ в переменную окружения OPENWEATHER_API_KEY:
   Для fish: set -x OPENWEATHER_API_KEY "ваш_ключ"

Использование:
   python3 pogoda.py              # спросит город
   python3 pogoda.py London       # возьмёт город из аргумента
"""

import os
import sys
import requests


def get_api_key():
	key = os.environ.get("OPENWEATHER_API_KEY")
	if not key:
		print("Не найден OPENWEATHER_API_KEY. Установите его перед запуском.")
		print("Пример для fish: set -x OPENWEATHER_API_KEY \"ваш_ключ\"")
		return None
	return key


def fetch_weather(city: str, api_key: str):
	url = (
		"https://api.openweathermap.org/data/2.5/weather"
	)
	params = {"q": city, "appid": api_key, "units": "metric", "lang": "ru"}
	try:
		resp = requests.get(url, params=params, timeout=10)
		resp.raise_for_status()
	except requests.RequestException as e:
		return {"error": f"Сетевой/HTTP-ошибка: {e}"}

	try:
		data = resp.json()
	except ValueError:
		return {"error": "Не удалось распарсить JSON ответа"}

	if data.get("cod") != 200:
		# OpenWeatherMap возвращает код ошибки в теле при ошибке
		message = data.get("message", "неизвестная ошибка")
		return {"error": f"API ошибка: {message}"}

	return {"data": data}


def pretty_print(data: dict):
	main = data.get("main", {})
	weather = data.get("weather", [{}])[0]
	wind = data.get("wind", {})

	name = data.get("name", "-")
	desc = weather.get("description", "-")
	temp = main.get("temp")
	feels = main.get("feels_like")
	humidity = main.get("humidity")
	wind_speed = wind.get("speed")

	print(f"Погода в {name}:")
	print(f"  Описание : {desc}")
	if temp is not None:
		print(f"  Температура: {temp}°C (ощущается как {feels}°C)")
	if humidity is not None:
		print(f"  Влажность : {humidity}%")
	if wind_speed is not None:
		print(f"  Ветер     : {wind_speed} м/с")


def main():
	api_key = get_api_key()
	if not api_key:
		return

	if len(sys.argv) > 1:
		city = " ".join(sys.argv[1:])
	else:
		city = input("Введите город (например, Almaty): ").strip()

	if not city:
		print("Город не указан")
		return

	result = fetch_weather(city, api_key)
	if "error" in result:
		print(result["error"])
		return

	pretty_print(result["data"])


if __name__ == "__main__":
	main()