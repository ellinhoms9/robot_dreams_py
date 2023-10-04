import pytest


def division_two_numbers(a, b):
    return a / b > 0


def test_division_two_numbers_positive():
    result = division_two_numbers(6, 3)
    assert result is True


def test_division_two_numbers_negative():
    result = division_two_numbers(3, 6)
    assert result is False


def test_division_two_numbers_zero_divisor():
    with pytest.raises(ZeroDivisionError):
        division_two_numbers(10, 0)


def test_division_two_numbers_input_types():
    result = division_two_numbers(6, 3)
    assert isinstance(result, bool)

    result = division_two_numbers(3, 6)
    assert isinstance(result, bool)

    with pytest.raises(TypeError):
        division_two_numbers("6", 3)

    with pytest.raises(TypeError):
        division_two_numbers(6, "3")

    with pytest.raises(TypeError):
        division_two_numbers("6", "3")
