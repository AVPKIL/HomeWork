from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""

    # Удаляем все пробелы из номера карты, если они есть
    card_number = card_number.replace(" ", "")

    # Проверяем, что номер карты состоит только из цифр и имеет длину 16 символов
    if not card_number.isdigit() or len(card_number) != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр")

    # Разбиваем номер карты по блокам по 4 цифры с пробелами
    block1 = card_number[:4]
    block2 = card_number[4:6] + "**"
    block3 = "****"
    block4 = card_number[12:16]

    # Объединяем блоки с пробелами
    masked_number = f"{block1} {block2} {block3} {block4}"

    return masked_number


def get_mask_account(account_number: Union[str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""

    # Удаляем все пробелы из номера счёта, если они есть
    account_number = str(account_number).replace(" ", "")

    # Проверяем, что номер счёта состоит только из цифр и имеет длину 20 символов
    if not account_number.isdigit() or len(account_number) != 20:
        raise ValueError("Номер счёта должен состоять из 20 цифр")

    masked_account = f"{'**'}{account_number[-4:]}"

    return masked_account
