from typing import Any
import masks


def mask_account_card(data: Any) -> str:
    """
    Принимает тип и номер карты одной строкой,
    Выводит тип карты/счет и замаскированный номер.

    """
    #Разделяем строку на тип и номер
    type_and_number = data.split()
    type_ = ' '.join(type_and_number[0:-1])
    number_ = type_and_number[-1]

    #Маскируем с помощью ранее созданных функций
    if type_ == 'Счет':
        #Маскировка для счета
        return f'{type_} {masks.get_mask_account(number_)}'
    else:
        #Маскировка для карт
        return f'{type_} {masks.get_mask_card_number(number_)}'


def get_date(date_str):
    """
    Преобразует строку с датой из формата 'ГГГГ-ММ-ДДТЧЧ:ММ:СС.СССССС'
    в формат 'ДД.ММ.ГГГГ'.

    """
    # Разделяем строку по символу 'T', чтобы получить только дату
    date_part = date_str.Split('T')[0]

    # Разделяем дату по дефисам
    year, month, day = date_part.Split('-')

    # Формируем строку в нужном формате
    return f"{day}.{month}.{year}"