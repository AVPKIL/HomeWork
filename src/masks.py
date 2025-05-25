from typing import Union
import logging


# Создаем отдельный объект логгера
logger = logging.getLogger('masks')
# Настраиваем file_handler для логгера
file_handler = logging.FileHandler(
    'logs/masks.log',
    mode='w',
    encoding='utf-8'
)
# Настраиваем file_formatter для логгера
file_formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# Устанавливаем форматер для handler
file_handler.setFormatter(file_formatter)
# Добавляем handler к логгеру
logger.addHandler(file_handler)
# Устанавливаем уровень логирования не меньше DEBUG
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    logger.debug(f"Начало обработки номера карты: {card_number}")

    try:
        # Удаляем все пробелы из номера карты, если они есть
        card_number = str(card_number).replace(" ", "")
        logger.debug(f"Номер карты после удаления пробелов: {card_number}")

        # Проверяем, что номер карты состоит только из цифр и имеет длину 16 символов
        if not card_number.isdigit() or len(card_number) != 16:
            error_msg = "Номер карты должен состоять из 16 цифр"
            # Логирование ошибочных случаев с уровнем не ниже ERROR
            logger.error(error_msg)
            raise ValueError(error_msg)

        # Разбиваем номер карты по блокам по 4 цифры с пробелами
        block1 = card_number[:4]
        block2 = card_number[4:6] + "**"
        block3 = "****"
        block4 = card_number[12:16]

        # Объединяем блоки с пробелами
        masked_number = f"{block1} {block2} {block3} {block4}"
        # Логирование успешных случаев
        logger.info(f"Успешно сгенерирована маска карты: {masked_number}")

        return masked_number

    except Exception as e:
        # 9-10. Логирование ошибочных случаев с уровнем ERROR
        logger.error(f"Ошибка при обработке номера карты: {e}", exc_info=True)
        raise


def get_mask_account(account_number: Union[str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    logger.debug(f"Начало обработки номера счета: {account_number}")

    try:
        # Удаляем все пробелы из номера счёта, если они есть
        account_number = str(account_number).replace(" ", "")
        logger.debug(f"Номер счета после удаления пробелов: {account_number}")

        # Проверяем, что номер счёта состоит только из цифр и имеет длину 20 символов
        if not account_number.isdigit() or len(account_number) != 20:
            error_msg = "Номер счёта должен состоять из 20 цифр"
            # Логирование ошибочных случаев с уровнем не ниже ERROR
            logger.error(error_msg)
            raise ValueError(error_msg)

        masked_account = f"{'**'}{account_number[-4:]}"
        # Логирование успешных случаев
        logger.info(f"Успешно сгенерирована маска счета: {masked_account}")

        return masked_account

    except Exception as e:
        # Логирование ошибочных случаев с уровнем ERROR
        logger.error(f"Ошибка при обработке номера счета: {e}", exc_info=True)
        raise
