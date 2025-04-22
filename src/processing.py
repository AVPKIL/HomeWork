def filter_by_state(list_dict: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """ Фильтрация списка словарей по значению ключа 'state'."""

    filtered_list = []
    for i in list_dict:
        if i.get('state') == state:
            filtered_list.append(i)
    return filtered_list


def sort_by_date(list_dict: list[dict], reverse: bool = True) -> list[dict]:
    """Функция возвращает список отсортированный по дате"""


    return sorted(list_dict, key=lambda x: x['date'], reverse=reverse)
