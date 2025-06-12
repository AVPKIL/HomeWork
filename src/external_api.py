import os
import requests
from typing import Any
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env файла

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(amount: float, currency: str) -> Any:
    """Конвертирует сумму в рубли по текущему курсу."""

    if currency.upper() == "RUB":
        return amount

    try:
        response = requests.get(BASE_URL, params={"base": currency, "symbols": "RUB"}, headers={"apikey": API_KEY})
        response.raise_for_status()

        data = response.json()
        rate = data["rates"]["RUB"]
        return amount * rate

    except (requests.RequestException, KeyError) as e:
        print(f"Ошибка при конвертации валюты: {e}")
        return 0.0
