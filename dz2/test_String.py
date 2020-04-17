import pytest


@pytest.mark.parametrize("test_input", ["Lorem ipsuM Dolor sit Amet"])
def test_string_lower_one(test_input):
    t_string = test_input.lower()
    assert t_string == "lorem ipsum dolor sit amet"


def test_string_upper_one():
    t_string = "lorem ipsum dolor sit amet"
    upper_string = t_string.upper()
    assert upper_string == "LOREM IPSUM DOLOR SIT AMET"


def test_string_find_one():
    t_string = "lorem ipsum dolor sit amet"
    finded_string = t_string.find("amet")
    assert finded_string == 22


def test_string_len_one():
    t_string = "lorem ipsum dolor sit amet"
    len_of_string = len(t_string)
    assert len_of_string == 26


def test_string_len_two():
    t_string = "123123142342343"
    len_of_string = len(t_string)
    assert len_of_string == 15
