def test_list_append_one(fixture_with_params):
    test_list = []
    test_list.append(fixture_with_params)
    assert test_list[0] == fixture_with_params


def test_list_append_two():
    test_list = []
    test_list.append(1)
    assert test_list[0] == 1


def test_list_remove_one():
    test_list = [1, 2, 3, 4]
    test_list.remove(4)
    assert test_list[-1] == 3


def test_list_remove_two():
    test_list = [1, 2, 1, 3, 4]
    test_list.remove(1)
    assert test_list == [2, 1, 3, 4]


def test_list_sort_one():
    test_list = [5, 2, 4, 3, 1]
    test_list.sort()
    assert test_list == [1, 2, 3, 4, 5]