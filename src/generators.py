from typing import List, Dict, Any, Generator, Iterator

def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator[dict[str, Any], Any, None]:
    """Фильтрует транзакции по заданной валюте и возвращает итератор."""

    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except (KeyError, TypeError):
            continue


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, который возвращает описания транзакций по очереди."""

    for transaction in transactions:
        try:
            yield transaction["description"]
        except (KeyError, TypeError):
            continue


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX."""

    if start < 1:
        raise ValueError("Начальное значение не может быть меньше 1")
    if end > 9999999999999999:
        raise ValueError("Конечное значение не может превышать 9999999999999999")
    if start > end:
        raise ValueError("Начальное значение не может быть больше конечного")

    for number in range(start, end + 1):
        # Форматируем число в 16-значную строку с ведущими нулями
        card_num = f"{number:016d}"
        # Разбиваем на группы по 4 цифры с пробелами
        yield f"{card_num[:4]} {card_num[4:8]} {card_num[8:12]} {card_num[12:16]}"
