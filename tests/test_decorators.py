from typing import Any
import pytest

from src.decorators import log


def test_log_to_console(capsys: Any) -> None:
    """Проверка лога в консоль при успешном выполнении."""

    @log()
    def add(a: Any, b: Any) -> Any:
        return a + b

    result = add(2, 3)

    # Получаем вывод в консоль
    captured = capsys.readouterr()
    logs = captured.out.strip().split("\n")

    # Проверяем логи
    assert len(logs) == 2
    assert "add started at" in logs[0]
    assert "add ok. Result: 5" in logs[1]


def test_log_error_to_console(capsys: Any) -> Any:
    """Проверка лога ошибки в консоль."""

    @log()
    def divide(a: Any, b: Any) -> Any:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    logs = captured.out.strip().split("\n")

    assert len(logs) == 2
    assert "divide started at" in logs[0]
    assert "divide error: ZeroDivisionError" in logs[1]
    assert "Inputs: (10, 0), {}" in logs[1]


def test_log_to_file(tmp_path: Any) -> Any:
    """Проверка лога в файл."""

    log_file = tmp_path / "test_log.txt"

    @log(filename=log_file)
    def multiply(a: Any, b: Any) -> Any:
        return a * b

    result = multiply(3, 4)
    assert result == 12

    # Читаем файл
    with open(log_file, "r") as f:
        logs = f.read().strip().split("\n")

    assert len(logs) == 2
    assert "multiply started at" in logs[0]
    assert "multiply ok. Result: 12" in logs[1]


def test_log_error_to_file(tmp_path: Any) -> Any:
    """Проверка лога ошибки в файл."""

    log_file = tmp_path / "error_log.txt"

    @log(filename=log_file)
    def fail() -> Any:
        raise ValueError("Oops!")

    with pytest.raises(ValueError):
        fail()

    with open(log_file, "r") as f:
        logs = f.read().strip().split("\n")

    assert len(logs) == 2
    assert "fail started at" in logs[0]
    assert "fail error: ValueError" in logs[1]
    assert "Inputs: (), {}" in logs[1]
