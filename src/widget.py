from typing import Any

from srs.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: Any) -> str:
    """
    Принимает тип и номер карты одной строкой,
    Выводит тип карты/счет и замаскированный номер.

    """
    type_and_number = data.split()
    type_ = " ".join(type_and_number[0:-1])
    number_ = type_and_number[-1]

    if type_ == "Счет":
        return f"{type_} {get_mask_account(number_)}"
    else:
        return f"{type_} {get_mask_card_number(number_)}"


def get_date(date_str: Any) -> str:
    """
    Преобразует строку с датой из формата 'ГГГГ-ММ-ДДТЧЧ:ММ:СС.СССССС'
    в формат 'ДД.ММ.ГГГГ'.

    """
    date_part = date_str.split("T")[0]

    year, month, day = date_part.split("-")

    return f"{day}.{month}.{year}"
