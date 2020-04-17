import pytest


@pytest.mark.parametrize("test_input", ["test"])
def test_remove_one(test_input):
    num_set = {4, "январь", "test", 0, "$"}
    num_set.remove(test_input)
    assert (test_input in num_set) == False


def test_add_one():
    num_set = {4, "январь", 0, "$"}
    num_set.add("test")
    assert ("test" in num_set) == True


def test_copy_one():
    num_set = {1, 2, 3, 4}
    copy_num_set = num_set.copy()
    assert copy_num_set == {1, 2, 3, 4}


def test_copy_one():
    num_set = {1, 2, 3, 4}
    copy_num_set = num_set.copy()
    assert copy_num_set == {1, 2, 3, 4}


def test_clear_one():
    num_set = {1, 2, 3, 4}
    num_set.clear()
    print(num_set)
    assert num_set == set()


def test_len_one():
    num_set = {1, 2, 3, 4}
    len_num_set = len(num_set)
    assert len_num_set == 4
