from typing import Any


def get_mask_card_number(card_number: str) -> str:
    """Маскировка цифр номера карты"""
    # Преобразуем номер в строку для удобной работы с символами
    card_str = str(card_number)
    # В случае наличия пробелов убираем их
    cleaned_card_str = card_str.replace(' ', '')
    # Проверяем, что длина номера достаточна для маскирования
    if len(cleaned_card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Выделяем видимые части: первые 6 и последние 4 цифры
    visible_start = cleaned_card_str[:6]
    visible_end = cleaned_card_str[-4:]

    # Разбиваем на блоки по 4 символа, разделяя пробелами
    result = f"{visible_start[:4]} {visible_start[4:6]}** **** {visible_end}"

    return result


def get_mask_account(account_number: str) -> str:
    """Маскировка цифр номера счета"""
    # Преобразуем номер в строку для удобной работы с символами
    account_number_str = str(account_number)
    cleaned_account_number_str = account_number_str.replace(' ', '')

    # Проверяем, что длина номера достаточна для маскирования
    if len(cleaned_account_number_str) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")

    # Выделяем видимые части: последние 4 цифры
    visible_end = cleaned_account_number_str[-4:]

    # Разбиваем на блоки по 4 символа, разделяя пробелами
    result = f"**{visible_end}"

    return result

