import pytest


@pytest.mark.parametrize("test_input", ["test"])
def test_dict_get_one(test_input):
    d = {"first": test_input}
    assert d.get("first") == test_input


def test_dict_get_two():
    d = {"first": 1}
    assert d.get("first") == 1


def test_dict_copy_one():
    d = {"first": 1}
    d_copy = d.copy()
    assert d_copy == {'first': 1}


def test_dict_clear_one():
    d = {"first": 1}
    d_clear = d.clear()
    assert d_clear == None


def test_dict_values_one():
    d = {"first": 1, "second" : 2}
    d_values = d.values()
    assert list(d_values) == [1, 2]
    print(d_values)