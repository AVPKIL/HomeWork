import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_valid_card_masking() -> None:
    """Тест корректного маскирования номера карты"""
    # Стандартный формат без пробелов
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"

    # Формат с пробелами
    assert get_mask_card_number("1234 5678 9012 3456") == "1234 56** **** 3456"

    # Проверка граничных значений (первый и последний блок)
    assert get_mask_card_number("1111222233334444") == "1111 22** **** 4444"


def test_invalid_card_numbers(error_number: str) -> None:
    """Тест обработки невалидных номеров карт"""
    # Неправильная длина
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("123456789012345")  # 15 цифр
    assert str(exc_info.value) == error_number

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("12345678901234567")  # 17 цифр
    assert str(exc_info.value) == error_number

    # Содержит не цифры
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("1234abcd56789012")
    assert str(exc_info.value) == error_number

    # Пустая строка
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == error_number


def test_edge_cases() -> None:
    """Тест нестандартных случаев"""
    # Все нули
    assert get_mask_card_number("0000000000000000") == "0000 00** **** 0000"

    # Пробелы в начале/конце
    assert get_mask_card_number("  1234567890123456  ") == "1234 56** **** 3456"

    # Множественные пробелы между цифрами
    assert get_mask_card_number("1234  5678  9012  3456") == "1234 56** **** 3456"


def test_input_types() -> None:
    """Тест обработки разных типов ввода (если Union[str] предполагает другие типы)"""
    # Число вместо строки (если функция должна это обрабатывать)
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        # Стандартные валидные номера счетов
        ("12345678901234567890", "**7890"),
        ("00000000000000000000", "**0000"),
        ("99999999999999999999", "**9999"),
        # Номера с пробелами (должны нормализоваться)
        ("1234 5678 9012 3456 7890", "**7890"),
        ("  12345678901234567890  ", "**7890"),
        ("12 3456 7890 1234 5678 90", "**7890"),
        # Граничные случаи
        ("11111111111111111111", "**1111"),
        ("99999999999999999999", "**9999"),
    ],
)
def test_valid_account_masking(account_number: str, expected: str) -> None:
    """Тестирование корректного маскирования валидных номеров счетов"""
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "account_number, error_message",
    [
        # Неправильная длина
        ("1234567890123456789", "Номер счёта должен состоять из 20 цифр"),  # 19 цифр
        ("123456789012345678901", "Номер счёта должен состоять из 20 цифр"),  # 21 цифра
        # Содержит нецифровые символы
        ("1234567890abcdefghij", "Номер счёта должен состоять из 20 цифр"),
        ("1234-5678-9012-3456-7890", "Номер счёта должен состоять из 20 цифр"),
        # Пустые строки
        ("", "Номер счёта должен состоять из 20 цифр"),
        ("      ", "Номер счёта должен состоять из 20 цифр"),
    ],
)
def test_invalid_account_numbers(account_number: str, error_message: str) -> None:
    """Тестирование обработки невалидных номеров счетов"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_number)
    assert str(exc_info.value) == error_message


@pytest.mark.parametrize(
    "account_number, expected",
    [
        # Проверка последних 4 цифр
        ("45400236323194784321", "**4321"),
        ("92519983999377998765", "**8765"),
        ("12345678901234567890", "**7890"),
    ],
)
def test_account_last_digits(account_number: str, expected: str) -> None:
    """Тестирование корректного отображения последних 4 цифр"""
    assert get_mask_account(account_number) == expected
