import json
from typing import List, Dict, Any
import logging

# Создаем отдельный объект логгера
logger = logging.getLogger('utils')
# Настраиваем file_handler для логгера
file_handler = logging.FileHandler(
    'logs/utils.log',
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


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает данные о транзакциях из JSON-файла."""
    logger.debug(f"Попытка загрузить данные из файла: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.debug(f"Успешно прочитаны данные из файла: {file_path}")

            # Проверяем, что данные являются списком
            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций из файла {file_path}")
                return data

            logger.warning(f"Файл {file_path} не содержит список транзакций")
            return []

    # Логирование ошибочных случаев с уровнем ERROR
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {str(e)}")
        return []

    except Exception as e:
        logger.error(f"Неожиданная ошибка при загрузке файла {file_path}: {str(e)}", exc_info=True)
        return []
