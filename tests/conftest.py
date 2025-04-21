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