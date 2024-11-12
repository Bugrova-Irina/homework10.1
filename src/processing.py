def filter_by_state(list_of_dicts: list[dict[str, any]], state: str = "EXECUTED") -> list[dict[str, any]]:
    """Функция, фильтрующая список по статусу"""
    new_list_of_dicts = []

    for dictionary in list_of_dicts:
        for value in dictionary.values():
            if value == state:
                new_list_of_dicts.append(dictionary)
    return new_list_of_dicts


def sort_by_date(list_of_dicts: list[dict[str, any]], reverse: bool = True) -> list[dict[str, any]]:
    """Функция, сортирующая список по дате"""
    sorted_list_of_dicts = sorted(list_of_dicts, key=lambda dictionary: dictionary["date"], reverse=reverse)
    return sorted_list_of_dicts
