from hexorcist import to_decimal, from_decimal

def test_to_decimal_valid_inputs():
    assert to_decimal("1010", 2) == 10
    assert to_decimal("A", 16) == 10
    assert to_decimal("Z", 36) == 35
    assert to_decimal("123", 10) == 123
    assert to_decimal("0", 10) == 0

def test_to_decimal_invalid_base():
    try:
        to_decimal("1010", 1)
    except ValueError as e:
        assert str(e) == "original_base must be between 2 and 36"
    try:
        to_decimal("1010", 37)
    except ValueError as e:
        assert str(e) == "original_base must be between 2 and 36"

def test_to_decimal_invalid_character():
    try:
        to_decimal("1G", 16)
    except ValueError as e:
        assert str(e) == "Digit 'G' not valid for base 16"
    try:
        to_decimal("123", 2)
    except ValueError as e:
        assert str(e) == "Digit '3' not valid for base 2"

def test_from_decimal_valid_inputs():
    assert from_decimal(10, 2) == "1010"
    assert from_decimal(10, 16) == "A"
    assert from_decimal(35, 36) == "Z"
    assert from_decimal(123, 10) == "123"
    assert from_decimal(0, 10) == "0"