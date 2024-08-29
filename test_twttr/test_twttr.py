import pytest
from twttr import shorten

def test_vowel_replacement():
    assert shorten("Twitter") == "Twttr", "Failed to remove vowels from 'Twitter'"

def test_capitalized_vowel_replacement():
    assert shorten("TWITTER") == "TWTTR", "Failed to remove capitalized vowels from 'TWITTER'"

def test_lowercase_vowel_replacement():
    assert shorten("twitter") == "twttr", "Failed to remove lowercase vowels from 'twitter'"

def test_mixed_case_vowel_replacement():
    assert shorten("TwItTeR") == "TwtTR", "Failed to handle mixed case vowels in 'TwItTeR'"

def test_number_handling():
    assert shorten("T3st1ng123") == "T3st1ng123", "Numbers should not be removed"

def test_no_vowels():
    assert shorten("TWTTR") == "TWTTR", "String with no vowels should remain unchanged"

# def test_punctuation_handling():
#     assert shorten("Twi,tter!") == "Twttr!", "Failed to handle punctuation in 'Twi,tter!'"

if __name__ == "__main__":
    pytest.main()
