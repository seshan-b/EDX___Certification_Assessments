import pytest
from plates import is_valid

def test_valid_plates():
    assert is_valid("AB123") == True
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("AB") == True

def test_plate_without_alphabetical_start():
    assert is_valid("123ABC") == False  # Plate does not start with two alphabetic characters
    assert is_valid("1A23BC") == False  # Plate starts with a digit instead of two letters
    assert is_valid("12AB") == False    # Plate starts with two digits
    assert is_valid("!@ABC") == False   # Plate starts with non-alphabetic characters
    assert is_valid(" ") == False   # Plate starts with non-alphabetic characters

def test_plate_length():
    assert is_valid("A") == False  # Too short, less than 2 characters
    assert is_valid("ABCDEFG") == False  # Too long, more than 6 characters

def test_number_placement():
    assert is_valid("AAA22A") == False  # Invalid because number is not at the end
    assert is_valid("CS5O") == False  # Invalid because letter 'O' is after the number

def test_zero_placement():
    assert is_valid("CS05") == False  # Invalid because '0' is not allowed in leading position of numbers

def test_alphanumeric_characters():
    assert is_valid("AB@CDE") == False  # Invalid because '@' is not allowed
    assert is_valid("CS 50") == False  # Invalid because spaces are not allowed
    assert is_valid("CS.50") == False  # Invalid because periods are not allowed

if __name__ == "__main__":
    pytest.main()
