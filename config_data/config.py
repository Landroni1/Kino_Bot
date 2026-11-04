import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены, отсутствует файл .env")
else:
    load_dotenv()

API_URL = "https://api.poiskkino.dev/v1.4/movie/search"
BOT_TOKEN = os.getenv("BOT_TOKEN")

HEADERS = {"X-API-Key": os.getenv("RAPID_API_KEY"), "accept": "application/json"}

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("search_films", "Поиск фильмов"),
    ("help", "Вывести справку"),
    ("stop", "Остановить поиск"),
)
