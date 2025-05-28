import requests
from datetime import datetime
import pytz
import psycopg2

# ID остановок
from_stop = 's9744837'  # Бутово
to_stop = 'c10747'  # Подольск

# Текущая дата и время в Московском часовом поясе
timezone = pytz.timezone('Europe/Moscow')
current_datetime = datetime.now(timezone)
current_date = current_datetime.strftime('%Y-%m-%d')
current_time = current_datetime.strftime('%H:%M')

# URL API Яндекс Расписания
url = f"https://api.rasp.yandex.net/v3.0/search/?apikey=a35156ba-b01f-4625-b424-21ef0ae0ce52&format=json&from={from_stop}&to={to_stop}&date={current_date}"

response = requests.get(url)
data = response.json()

print(f"Расписание на {current_date.replace('-', '/')} (текущее время: {current_time}):\n")

if 'segments' in data:
    for segment in data['segments']:
        departure_time_str = segment['departure']  # "2025-05-26T23:01:00+03:00"
        arrival_time_str = segment['arrival']  # "2025-05-26T23:47:00+03:00"

        # Парсим время отправления и прибытия
        departure_dt = datetime.strptime(departure_time_str, "%Y-%m-%dT%H:%M:%S%z")
        arrival_dt = datetime.strptime(arrival_time_str, "%Y-%m-%dT%H:%M:%S%z")

        # Форматируем в "26/05/2025 23:01"
        formatted_departure = departure_dt.strftime("%d/%m/%Y %H:%M")
        formatted_arrival = arrival_dt.strftime("%d/%m/%Y %H:%M")

        # Определяем статус рейса
        if departure_dt < current_datetime:
            status = "ушел"
        else:
            status = "ожидается"

        print(f"Рейс: {segment['thread']['title']}")
        print(f"Отправление: {formatted_departure}")
        print(f"Прибытие: {formatted_arrival}")
        print(f"Статус: {status}")
        print("-" * 30)
else:
    print("Нет данных о рейсах на сегодня.")