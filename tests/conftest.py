import pytest


@pytest.fixture
def error_number():
    return "Номер карты должен состоять из 16 цифр"


@pytest.fixture
def invalid_dates():
    """Фикстура возвращает список невалидных строк с датами"""
    return [
        "2023-04",  # Неполная дата
        "15.04.2023",  # Обратный формат
        "",  # Пустая строка
        "T12:30:45",  # Только время
        "Some random text",  # Текст
    ]


@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "amount": "100"},
        {"id": 2, "state": "PENDING", "amount": "200"},
        {"id": 3, "state": "EXECUTED", "amount": "300"},
        {"id": 4, "state": "CANCELED", "amount": "400"},
        {"id": 5, "state": "EXECUTED", "amount": "500"},
    ]


@pytest.fixture
def sample_date():
    return [
        {"id": 1, "date": "2023-04-15T12:30:45"},
        {"id": 2, "date": "2022-12-31T23:59:59"},
        {"id": 3, "date": "2023-01-01T00:00:01"},
        {"id": 4, "date": "2023-04-15T12:30:44"},
    ]
