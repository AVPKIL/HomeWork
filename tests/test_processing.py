import pytest

from src.processing import filter_by_state, sort_by_date


# Основные тесты с параметризацией
@pytest.mark.parametrize(
    "input_data, state, expected_ids",
    [
        # Стандартные случаи
        (
            [
                {"id": 1, "state": "EXECUTED", "amount": "100"},
                {"id": 2, "state": "PENDING", "amount": "200"},
                {"id": 3, "state": "EXECUTED", "amount": "300"},
            ],
            "EXECUTED",
            [1, 3],
        ),
        # Один элемент в результате
        (
            [
                {"id": 1, "state": "PENDING", "amount": "100"},
                {"id": 2, "state": "CANCELED", "amount": "200"},
            ],
            "PENDING",
            [1],
        ),
        # Нет совпадений
        (
            [
                {"id": 1, "state": "EXECUTED", "amount": "100"},
                {"id": 2, "state": "EXECUTED", "amount": "200"},
            ],
            "CANCELED",
            [],
        ),
        # Пустой входной список
        ([], "EXECUTED", []),
        # Значение по умолчанию (state='EXECUTED')
        (
            [
                {"id": 1, "state": "EXECUTED", "amount": "100"},
                {"id": 2, "state": "PENDING", "amount": "200"},
            ],
            None,
            [1],
        ),
        # Словари без ключа 'state'
        (
            [
                {"id": 1, "amount": "100"},
                {"id": 2, "state": "EXECUTED", "amount": "200"},
            ],
            "EXECUTED",
            [2],
        ),
    ],
)
def test_filter_by_state(input_data, state: str, expected_ids) -> None:
    """Параметризованный тест для различных сценариев фильтрации"""
    if state is None:
        result = filter_by_state(input_data)
    else:
        result = filter_by_state(input_data, state)


VALID_DATE = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

DUPLICATE_DATES = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},  # Полное совпадение с id 41428829
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

INVALID_DATES = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},  # Без времени
    {"id": 615064591, "state": "CANCELED", "date": "14.04.2023"},  # Неправильный формат
    {"id": 594226727, "state": "CANCELED", "date": "September 12, 2018"},
]  # Текстовый формат


def test_sort_valid_dates():
    """Тесты для корректных дат"""
    # По убыванию (reverse=True)
    assert sort_by_date(VALID_DATE, True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    # По возрастанию (reverse=False)
    assert sort_by_date(VALID_DATE, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


# Тесты для одинаковых дат
def test_duplicate_dates():
    """Тестирование сортировки при одинаковых датах"""
    result = sort_by_date(DUPLICATE_DATES, reverse=True) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


# Тесты для нестандартных форматов
def test_no_correct_dates():
    """Тестирование сортировки при одинаковых датах"""
    result = sort_by_date(INVALID_DATES, reverse=True) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]
