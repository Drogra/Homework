import pytest

from srs.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number1():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("7000 7922 8960 6361") == "7000 79** **** 6361"
    assert get_mask_card_number("1596837868705199") == "1596 83** **** 5199"
    assert get_mask_card_number("1596 8378 6870 5199") == "1596 83** **** 5199"

@pytest.mark.parametrize('card_number, expected_result', [
    ('7000792289606361','7000 79** **** 6361'),
    ('1596837868705199','1596 83** **** 5199'),
    ('7158300734726758','7158 30** **** 6758')
])
def test_get_mask_card_number2(card_number, expected_result):
    assert get_mask_card_number(card_number) == expected_result

def test_get_mask_card_number3():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("70007922896063612")

    assert str(exc_info.value) == "Номер карты должен содержать 16 цифр"


def test_get_mask_card_number4():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("700079228960636")

    assert str(exc_info.value) == "Номер карты должен содержать 16 цифр"


def test_get_mask_account1():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("736 54 108 4 3013 5874305") == "**4305"


def test_get_mask_account2():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("7365410843013587430521")

    assert str(exc_info.value) == "Номер счета должен содержать 20 цифр"
