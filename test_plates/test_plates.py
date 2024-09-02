import pytest
from plates import is_valid

def test_valid_plates():
    assert is_valid("AB123") == True
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("AB") == True

def test_plate_without_alphabetical_start():
    # Test cases that should return False because the plate does not start with at least two letters
    invalid_plates = ["123ABC", "1A23BC", "12AB", "!@ABC"]

    for plate in invalid_plates:
        assert is_valid(plate) == False

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

def test_exit_code_for_alphabetical_check(monkeypatch):
    # Test cases that should cause the main program to exit with code 1 due to invalid start
    invalid_plates = ["123ABC", "1A23BC", "12AB", "!@ABC"]

    for plate in invalid_plates:
        monkeypatch.setattr('builtins.input', lambda _: plate)
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 1  # Expect exit code 1 for invalid plates

