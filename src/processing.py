def filter_by_state(list_of_dicts: list, state="EXECUTED") -> list:
    """Функция, которая фильтрует список по статусу"""
    new_list_of_dicts = []

    for dict in list_of_dicts:
        for value in dict.values():
            if value == state:
                new_list_of_dicts.append(dict)
    return new_list_of_dicts
