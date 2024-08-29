from twttr import shorten

# Test cases

# Basic vowel removal
def test_basic_vowel_removal():
    assert shorten("Twitter") == "Twttr", "Failed to remove vowels from 'Twitter'"

# Capitalized vowel removal
def test_capitalized_vowel_removal():
    assert shorten("TWITTER") == "TWTTR", "Failed to remove capitalized vowels from 'TWITTER'"

# Lowercase vowel removal
def test_lowercase_vowel_removal():
    assert shorten("twitter") == "twttr", "Failed to remove lowercase vowels from 'twitter'"

# Mixed case vowel removal
def test_mixed_case_vowel_removal():
    assert shorten("TwItTeR") == "TwtTR", "Failed to handle mixed case vowels in 'TwItTeR'"

# Ensure numbers are not removed
def test_number_handling():
    assert shorten("T3st1ng123") == "T3st1ng123", "Numbers should not be removed"

# No vowels to remove
def test_no_vowels():
    assert shorten("TWTTR") == "TWTTR", "String with no vowels should remain unchanged"

# Punctuation handling
def test_punctuation_handling():
    assert shorten("Twi,tter!") == "Twttr!", "Failed to handle punctuation in 'Twi,tter!'"

if __name__ == "__main__":
    test_basic_vowel_removal()
    test_capitalized_vowel_removal()
    test_lowercase_vowel_removal()
    test_mixed_case_vowel_removal()
    test_number_handling()
    test_no_vowels()
    test_punctuation_handling()
    print("All tests passed!")
