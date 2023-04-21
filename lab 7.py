import requests
import random


# Згенеруємо випадковий ID
rand_id = random.randint(1, 100)

# Зробимо API динамічним, підставивши в URL номер ID
response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{rand_id}')

# Перевірка
if response.status_code == 200:

    # Розпарсимо відповідь в JSON форматі
    data = response.json()

    # Виведемо в консоль необхідні дані
    print(f"ID: {data['id']}\n")
    print(f"Title: {data['title']}\n")
    print(f"Body: {data['body']}")
else:
    print("Помилка. Не вдалося витягти дані з API.")
