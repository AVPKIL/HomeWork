# from src.masks import get_mask_card_number, get_mask_account
#
#
# def demonstrate_masks_module():
#     print("Демонстрация работы модуля masks:")
#     print("\n1. Корректные данные:")
#
#     # Пример с корректным номером карты
#     card_number = "1234567890123456"
#     print(f"\nМаскирование номера карты: {card_number}")
#     try:
#         masked_card = get_mask_card_number(card_number)
#         print(f"Результат: {masked_card}")  # Ожидаемый результат: "1234 56** **** 3456"
#     except Exception as e:
#         print(f"Ошибка: {e}")
#
#     # Пример с корректным номером счета
#     account_number = "12345678901234567890"
#     print(f"\nМаскирование номера счета: {account_number}")
#     try:
#         masked_account = get_mask_account(account_number)
#         print(f"Результат: {masked_account}")  # Ожидаемый результат: "**7890"
#     except Exception as e:
#         print(f"Ошибка: {e}")
#
#     print("\n2. Ошибочные данные:")
#
#     # Пример с некорректным номером карты (слишком короткий)
#     invalid_card = "12345678"
#     print(f"\nПопытка маскирования неверного номера карты: {invalid_card}")
#     try:
#         result = get_mask_card_number(invalid_card)
#         print(f"Результат: {result}")
#     except Exception as e:
#         print(f"Ошибка: {e}")  # Ожидаем ошибку "Номер карты должен состоять из 16 цифр"
#
#     # Пример с некорректным номером счета (содержит буквы)
#     invalid_account = "ABCD5678901234567890"
#     print(f"\nПопытка маскирования неверного номера счета: {invalid_account}")
#     try:
#         result = get_mask_account(invalid_account)
#         print(f"Результат: {result}")
#     except Exception as e:
#         print(f"Ошибка: {e}")  # Ожидаем ошибку "Номер счёта должен состоять из 20 цифр"
#
#
# if __name__ == "__main__":
#     demonstrate_masks_module()


from src.utils import load_transactions


def demonstrate_utils_module():
    print("Демонстрация работы модуля utils:")

    # 1. Корректный файл
    print("\n1. Загрузка корректного файла:")
    transactions = load_transactions("data/valid_transactions.json")
    print(f"Загружено транзакций: {len(transactions)}")

    # 2. Несуществующий файл
    print("\n2. Попытка загрузки несуществующего файла:")
    transactions = load_transactions("data/nonexistent.json")
    print(f"Результат: {transactions}")

    # 3. Некорректный JSON
    print("\n3. Попытка загрузки битого JSON:")
    transactions = load_transactions("data/broken.json")
    print(f"Результат: {transactions}")


if __name__ == "__main__":
    demonstrate_utils_module()
