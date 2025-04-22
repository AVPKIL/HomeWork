from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """Обработка информации о картах и о счетах"""


    #Очищаем строку от лишних пробелов
    data = data.strip()
    if not data:
        return data

    parts = data.split(" ")
    if not parts:
        return data

    # Определяем тип (счет или карта)
    if len(parts) == 1:
        # Если только номер, пробуем определить по длине
        number_part = parts[0]
        try:
            if len(number_part.replace(" ", "")) == 20:
                return get_mask_account(number_part)
            elif len(number_part.replace(" ", "")) == 16:
                return get_mask_card_number(number_part)
            else:
                return data
        except ValueError:
            return data
    else:
        # Если есть название
        name_parts = parts[:-1]
        number_part = parts[-1]
        name = " ".join(name_parts)

        try:
            if name.lower() == "счет":
                masked_number = get_mask_account(number_part)
                return f"{name} {masked_number}"
            else:
                masked_number = get_mask_card_number(number_part)
                return f"{name} {masked_number}"
        except ValueError:
            return data



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
