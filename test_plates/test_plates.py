from plates import is_valid

def main():
    test_alphabetical_checks()
    test_length_checks()
    test_number_placement()
    test_zero_placement()
    test_alphanumeric_characters()

def test_alphabetical_checks():
    assert is_valid("AA") == True  # Valid: starts with two letters
    assert is_valid("A1") == False  # Invalid: starts with one letter
    assert is_valid("1A") == False  # Invalid: starts with a digit
    assert is_valid("11") == False  # Invalid: starts with two digits
    assert is_valid("a") == False   # Invalid: too short and lowercase
    assert is_valid("A") == False   # Invalid: too short

def test_length_checks():
    assert is_valid("ABCDEF") == True  # Valid: length exactly 6 characters
    assert is_valid("ABCDEFABC") == False  # Invalid: length more than 6 characters
    assert is_valid("a") == False   # Invalid: length less than 2 characters
    assert is_valid("A") == False   # Invalid: length less than 2 characters

def test_number_placement():
    assert is_valid("AAA111") == True  # Valid: numbers at the end
    assert is_valid("111AAA") == False  # Invalid: numbers at the beginning
    assert is_valid("AAA11A") == False  # Invalid: numbers mixed with letters
    assert is_valid("AAA11") == True    # Valid: numbers at the end

def test_zero_placement():
    assert is_valid("cs05") == False  # Invalid: first number is 0
    assert is_valid("cs50") == True   # Valid: no leading zero in numbers

def test_alphanumeric_characters():
    assert is_valid("some word") == False  # Invalid: contains a space
    assert is_valid("cs50") == True        # Valid: only alphanumeric characters
    assert is_valid(".!") == False         # Invalid: contains special characters
    assert is_valid("cs50!") == False      # Invalid: contains a special character at the end
    assert is_valid("cs 50") == False      # Invalid: contains a space

if __name__ == "__main__":
    main()
