from functions import add, divide, get_element, convert_to_integer


def test_add_numbers():
    result = add(2, 3)
    assert result == 5
    assert isinstance(result, int)


def test_divide_numbers():
    result = divide(10, 2)
    assert result == 5
    assert isinstance(result, float)


def test_get_valid_element():
    list_ = [1, 2, 3]
    assert get_element(list_, 1) == 2


def test_convert_valid_integer():
    result = convert_to_integer("5.5")
    assert result == 5
    assert isinstance(result, int)