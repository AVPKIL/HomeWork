import pytest
from unittest.mock import patch
from src.external_api import convert_to_rub


@patch("requests.get")
def test_convert_usd_to_rub(mock_get) -> None:
    """Тест конвертации в USD"""
    mock_get.return_value.json.return_value = {"rates": {"RUB": 82.30}}
    assert convert_to_rub(100, "USD") == 8230
    mock_get.assert_called_once()


@patch("requests.get")
def test_convert_eur_to_rub(mock_get) -> None:
    """Тест конвертации в EUR"""
    mock_get.return_value.json.return_value = {"rates": {"RUB": 91.3}}
    assert convert_to_rub(50, "EUR") == 4565
    mock_get.assert_called_once()


def test_convert_rub_to_rub() -> None:
    """Тест без конвертации"""
    result = convert_to_rub(1000, "RUB")
    assert result == 1000
