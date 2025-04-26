import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "рубли",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }
]


def test_filter_by_currency():
    # Тест на корректную фильтрацию
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268

    # Проверка, что итератор завершается
    with pytest.raises(StopIteration):
        next(usd_transactions)

    # Тест на другую валюту
    rub_transactions = filter_by_currency(transactions, "RUB")
    assert next(rub_transactions)["id"] == 873106923

    # Тест на несуществующую валюту
    eur_transactions = filter_by_currency(transactions, "EUR")
    with pytest.raises(StopIteration):
        next(eur_transactions)


def test_invalid_transactions():
    # Тест с некорректными данными транзакций
    invalid_transactions = [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},  # Корректная
        {"id": 2},  # Нет operationAmount
        {"id": 3, "operationAmount": {"currency": {}}},  # Нет code
        {"id": 4, "operationAmount": {"currency": {"code": "USD"}}},  # Корректная
        None,  # None вместо транзакции
    ]

    usd_transactions = filter_by_currency(invalid_transactions, "USD")
    assert next(usd_transactions)["id"] == 1
    assert next(usd_transactions)["id"] == 4

    with pytest.raises(StopIteration):
        next(usd_transactions)



def test_transaction_descriptions():
    # Создаем тестовые данные
    test_transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"no_description": "Нет нужного ключа"},  # Транзакция без описания
        {"description": "Перевод с карты на карту"},
        None,  # None вместо транзакции
        {"description": "Оплата услуг"},
        {"description": "Перевод по СБП"}
    ]

    # Получаем генератор
    desc_gen = transaction_descriptions(test_transactions)

    # Проверяем корректные описания
    assert next(desc_gen) == "Перевод организации"
    assert next(desc_gen) == "Перевод со счета на счет"
    assert next(desc_gen) == "Перевод с карты на карту"
    assert next(desc_gen) == "Оплата услуг"
    assert next(desc_gen) == "Перевод по СБП"

    # Проверяем завершение итератора
    with pytest.raises(StopIteration):
        next(desc_gen)


def test_empty_transactions():
    # Тест с пустым списком транзакций
    empty_gen = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(empty_gen)


def test_invalid_transactions_desc():
    # Тест с некорректными данными
    invalid_transactions = [
        {"id": 1},  # Нет описания
        None,
        {"description": "Valid description"},
        12345,  # Не словарь
        {"desc": "Неправильный ключ"}
    ]

    desc_gen = transaction_descriptions(invalid_transactions)
    assert next(desc_gen) == "Valid description"
    with pytest.raises(StopIteration):
        next(desc_gen)


def test_card_number_generator_basic():
    """Тест базового функционала"""
    generator = card_number_generator(1, 3)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"

    with pytest.raises(StopIteration):
        next(generator)

def test_card_number_generator_edge_cases():
    """Тест граничных случаев"""
    # Минимальное значение
    generator = card_number_generator(1, 1)
    assert next(generator) == "0000 0000 0000 0001"

    # Максимальное значение
    generator = card_number_generator(9999999999999999, 9999999999999999)
    assert next(generator) == "9999 9999 9999 9999"

def test_card_number_generator_invalid_range():
    """Тест обработки неверного диапазона"""

    with pytest.raises(ValueError):
        # Стартовое значение меньше 1
        list(card_number_generator(0, 5))

    with pytest.raises(ValueError):
        # Конечное значение больше 9999999999999999
        list(card_number_generator(1, 10000000000000000))

    with pytest.raises(ValueError):
        # Старт больше конца
        list(card_number_generator(10, 5))