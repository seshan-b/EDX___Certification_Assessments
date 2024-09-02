import pytest
from plates import is_valid

def test_valid_plates():
    # Plates that meet all the criteria should return True
    assert is_valid("AB123") == True
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("AB") == True
    assert is_valid("ABCD") == True    # Valid plate with only letters

def test_plate_without_alphabetical_start():
    # Plates that do not start with two alphabetic characters should return False
    invalid_plates = [
        "123ABC",  # Starts with digits
        "1A23BC",  # Starts with a digit
        "12ABC",   # Starts with two digits
        "!@ABCB",  # Starts with non-alphabetic characters
        "12ABCD",  # Starts with two digits
        "9X8YZ",   # Starts with a digit
        "7ABCD"    # Starts with a digit
    ]

    for plate in invalid_plates:
        assert is_valid(plate) == False

def test_plate_length():
    # Plates that are too short or too long should return False
    assert is_valid("A") == False      # Too short
    assert is_valid("ABCDEFG") == False  # Too long

def test_number_placement():
    # Plates that have numbers in invalid positions should return False
    assert is_valid("AAA22A") == False  # Invalid because number is not at the end
    assert is_valid("CS5O") == False    # Invalid because letter 'O' is after the number
    assert is_valid("AB1C2") == False   # Invalid because the number is in the middle
    assert is_valid("C123AB") == False  # Invalid because numbers are not at the end

def test_zero_placement():
    # Plates where the first number is '0' should return False
    assert is_valid("CS05") == False  # Invalid because '0' is not allowed as the leading digit

def test_alphanumeric_characters():
    # Plates containing invalid characters should return False
    assert is_valid("AB@CDE") == False  # Invalid because '@' is not allowed
    assert is_valid("CS 50") == False   # Invalid because spaces are not allowed
    assert is_valid("CS.50") == False   # Invalid because periods are not allowed
    assert is_valid("PLATE!") == False  # Invalid because '!' is not allowed
    assert is_valid("HELLO#") == False  # Invalid because '#' is not allowed

if __name__ == "__main__":
    pytest.main()
