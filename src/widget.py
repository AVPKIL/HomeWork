from os.path import split

from masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """Обработка информации о картах и о счетах"""

    parts = data.split(" ")
    if len(parts) < 2:
        return data

    # Собираем название (все части, кроме последней)
    name = " ".join(parts[:-1])
    number = parts[-1]

    # Обработка карты (если название не "Счет")
    if name.lower() != "счет":
        # Оставляем только цифры
        masked_number = get_mask_card_number(number)
        return f"{name} {masked_number}"

    # Обработка счета
    else:
        masked_number = get_mask_account(number)
        return f"{name} {masked_number}"


def get_date(data_str: str) -> str:
    """Функция, которая возвращает дату"""

    # Проверка на правильность формата даты
    try:
        # Разделяем строку по символу 'T' (дата и время)
        date_part = data_str.split("T")[0]

        # Разделяем дату на год, месяц и день
        year = date_part.split("-")[0]
        month = date_part.split("-")[1]
        day = date_part.split("-")[2]

        # Форматируем в "ДД.ММ.ГГГГ"
        return f"{day}.{month}.{year}"

    except (IndexError, ValueError):
        return "Некорректный формат даты"
