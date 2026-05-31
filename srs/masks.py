from typing import Any


def get_mask_card_number(card_number: Any) -> str:
    """Маскировка цифр номера карты"""
    # Преобразуем номер в строку для удобной работы с символами
    card_str = str(card_number)

    # Проверяем, что длина номера достаточна для маскирования
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать минимум 16 цифр")

    # Выделяем видимые части: первые 6 и последние 4 цифры
    visible_start = card_str[:6]
    visible_end = card_str[-4:]

    # Разбиваем на блоки по 4 символа, разделяя пробелами
    result = f"{visible_start[:4]} {visible_start[4:6]}** **** {visible_end}"

    return result


def get_mask_account(account_number: Any) -> str:
    """Маскировка цифр номера счета"""
    # Преобразуем номер в строку для удобной работы с символами
    account_number_str = str(account_number)

    # Проверяем, что длина номера достаточна для маскирования
    if len(account_number_str) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифр")

    # Выделяем видимые части: последние 4 цифры
    visible_end = account_number_str[-4:]

    # Разбиваем на блоки по 4 символа, разделяя пробелами
    result = f"**{visible_end}"

    return result
