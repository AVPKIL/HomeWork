from typing import Any
from functools import wraps
import datetime


def log(filename: Any = None) -> Any:
    """Декоратор для лога вызовов функций, их аргументов, результатов и ошибок."""

    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Формируем строку с входными аргументами
            inputs = f"Inputs: {args}, {kwargs}"

            # Запись в лог начало выполнения функции
            start_time = datetime.datetime.now()
            log_message_start = f"{func.__name__} started at {start_time}"

            if filename:
                with open(filename, "a") as f:
                    f.write(log_message_start + "\n")
            else:
                print(log_message_start)

            try:
                result = func(*args, **kwargs)
                # Запись в лог успешное завершение
                end_time = datetime.datetime.now()
                log_message_ok = f"{func.__name__} ok. Result: {result}."

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message_ok + "\n")
                else:
                    print(log_message_ok)

                return result

            except Exception as e:
                # Запись в лог ошибку
                end_time = datetime.datetime.now()
                log_message_error = f"{func.__name__} error: {type(e).__name__}. {inputs}."

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message_error + "\n")
                else:
                    print(log_message_error)

                raise  # Пробрасываем исключение дальше

        return wrapper

    return decorator
