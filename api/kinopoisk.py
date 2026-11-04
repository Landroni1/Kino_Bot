import logging

import requests
from requests.exceptions import ConnectionError, HTTPError, RequestException, Timeout

from config_data.config import API_URL, HEADERS

logging.basicConfig(
    filename="Api_errors.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8",
)


def get_movie_data(query):
    params = {"query": query, "limit": 10}
    try:
        response = requests.get(API_URL, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        if data.get("docs"):
            return data["docs"]

        logging.warning(f"Фильм '{query}' не найден.")
        return None

        # 2. Обрабатываем ТАЙМАУТ (сервер думал слишком долго)
    except Timeout:
        logging.error(f"Тайм-аут ожидания для: {query}")
        return None

        # 3. Обрабатываем ОШИБКИ СЕТИ (нет интернета, сервер упал, неверный URL)
    except ConnectionError:
        logging.error(
            f"Проблема с соединением (проверьте интернет или URL) для: {query}"
        )
        return None

        # 4. Обрабатываем ОШИБКИ HTTP (если response.raise_for_status()
        # поймал 4xx или 5xx)
    except HTTPError as e:
        logging.error(
            f"Ошибка сервера (статус {response.status_code}) для: {query}: {e}"
        )
        return None

        # 5. Обрабатываем ВСЕ ОСТАЛЬНЫЕ сетевые ошибки (общий класс)
    except RequestException as e:
        logging.error(f"Неизвестная ошибка библиотеки requests: {e}")
        return None

        # 6. Обрабатываем ОШИБКИ ПАРСИНГА (если JSON пришел кривой)
    except (ValueError, KeyError) as e:
        logging.error(f"Ошибка при разборе данных JSON: {e}")
        return None
