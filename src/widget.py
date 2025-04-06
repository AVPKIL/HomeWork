import masks


def mask_account_card(data: str)-> str:
    """Обработка информации о картах и о счетах"""

    parts = data.split(' ')
    if len(parts) < 2:
        return data

    # Собираем название (все части, кроме последней)
    name = ' '.join(parts[:-1])
    number = parts[-1]

    # Обработка карты (если название не "Счет")
    if name.lower() != 'счет':
        # Оставляем только цифры
        masked_number = masks.get_mask_card_number(number)
        return f"{name} {masked_number}"

    # Обработка счета
    else:
        masked_number = masks.get_mask_account(number)
        return f"{name} {masked_number}"
