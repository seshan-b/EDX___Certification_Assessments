import pytest
from plates import is_valid

# Test: valid plates pass all checks
def test_valid_plates():
    assert is_valid("AB123") == True
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("AB") == True

# Test: plates without beginning alphabetical checks
def test_plate_without_alphabetical_start():
    # Test cases that should return False because the plate does not start with at least two letters
    assert is_valid("123ABC") == False  # Fails because it doesn't start with letters
    assert is_valid("1A23BC") == False  # Fails because it starts with one digit
    assert is_valid("A1B2C3") == False  # Fails because second character is not a letter
    assert is_valid("12AB") == False    # Fails because it starts with two digits
    assert is_valid("!@ABC") == False   # Fails because it starts with non-alphabetical characters

# Test: plates without length checks
def test_plate_length():
    assert is_valid("A") == False  # Too short, less than 2 characters
    assert is_valid("ABCDEFG") == False  # Too long, more than 6 characters

# Test: plates without checks for number placement
def test_number_placement():
    assert is_valid("AAA22A") == False  # Invalid because number is not at the end
    assert is_valid("CS5O") == False  # Invalid because letter 'O' is after the number

# Test: plates without checks for zero placement
def test_zero_placement():
    assert is_valid("CS05") == False  # Invalid because '0' is not allowed in leading position of numbers

# Test: plates without checks for alphanumeric characters
def test_alphanumeric_characters():
    assert is_valid("AB@CDE") == False  # Invalid because '@' is not allowed
    assert is_valid("CS 50") == False  # Invalid because spaces are not allowed
    assert is_valid("CS.50") == False  # Invalid because periods are not allowed

# To run these tests, use the command: pytest test_plates.py
