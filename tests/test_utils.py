import pytest
from unittest.mock import mock_open, patch
from src.utils import load_transactions  # Изменён импорт

# Тестовые данные
TEST_TRANSACTIONS = """
[
    {
        "id": 441945886,
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"code": "RUB"}
        }
    },
    {
        "id": 41428829,
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"code": "USD"}
        }
    }
]
"""


def test_load_transactions_success() -> None:
    """Тест успешной загрузки транзакций из файла"""
    with patch("builtins.open", mock_open(read_data=TEST_TRANSACTIONS)):
        result = load_transactions("transactions.json")
        assert len(result) == 2
        assert result[0]["id"] == 441945886
        assert result[1]["operationAmount"]["currency"]["code"] == "USD"


def test_load_empty_file() -> None:
    """Тест загрузки пустого файла"""
    with patch("builtins.open", mock_open(read_data="")):
        result = load_transactions("empty.json")
        assert result == []


def test_load_invalid_json() -> None:
    """Тест загрузки невалидного JSON"""
    with patch("builtins.open", mock_open(read_data="invalid json")):
        result = load_transactions("invalid.json")
        assert result == []


def test_file_not_found() -> None:
    """Тест обработки отсутствующего файла"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_transactions("nonexistent.json")
        assert result == []


def test_non_list_json() -> None:
    """Тест загрузки JSON, который не является списком"""
    with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
        result = load_transactions("not_list.json")
        assert result == []
