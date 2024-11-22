
import psycopg2
from dotenv import load_dotenv
import os

print("Загрузка .env файла...")
load_dotenv()
print("Проверка переменных окружения:")
print("DB_NAME:", os.getenv("DB_NAME"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))

# Получаем настройки подключения
db_config = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}

print("Параметры подключения:", db_config)

# Подключение к базе данных
try:
    print("Пробую подключиться к базе данных...")
    conn = psycopg2.connect(**db_config)
    print("Успешное подключение к базе данных")

    cursor = conn.cursor()
    print("Создаём курсор и выполняем запрос...")

    # Выполняем тестовый запрос
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Версия базы данных: {db_version}")

    cursor.close()
    conn.close()
    print("Соединение закрыто")

except Exception as e:
    print(f"Ошибка подключения: {e}")