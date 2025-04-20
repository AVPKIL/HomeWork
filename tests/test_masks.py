import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_valid_card_masking():
    """Тест корректного маскирования номера карты"""
    # Стандартный формат без пробелов
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"

    # Формат с пробелами
    assert get_mask_card_number("1234 5678 9012 3456") == "1234 56** **** 3456"

    # Проверка граничных значений (первый и последний блок)
    assert get_mask_card_number("1111222233334444") == "1111 22** **** 4444"


def test_invalid_card_numbers():
    """Тест обработки невалидных номеров карт"""
    # Неправильная длина
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("123456789012345")  # 15 цифр
    assert str(exc_info.value) == "Номер карты должен состоять из 16 цифр"

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("12345678901234567")  # 17 цифр
    assert str(exc_info.value) == "Номер карты должен состоять из 16 цифр"

    # Содержит не цифры
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("1234abcd56789012")
    assert str(exc_info.value) == "Номер карты должен состоять из 16 цифр"

    # Пустая строка
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == "Номер карты должен состоять из 16 цифр"

def test_edge_cases():
    """Тест нестандартных случаев"""
    # Все нули
    assert get_mask_card_number("0000000000000000") == "0000 00** **** 0000"

    # Пробелы в начале/конце
    assert get_mask_card_number("  1234567890123456  ") == "1234 56** **** 3456"

    # Множественные пробелы между цифрами
    assert get_mask_card_number("1234  5678  9012  3456") == "1234 56** **** 3456"


def test_input_types():
    """Тест обработки разных типов ввода (если Union[str] предполагает другие типы)"""
    # Число вместо строки (если функция должна это обрабатывать)
    with pytest.raises(AttributeError):
        get_mask_card_number(1234567890123456)  # Передали int