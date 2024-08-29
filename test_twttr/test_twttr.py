

from twttr import shorten

def test_vowel_replacement():
    assert shorten("Twitter") == "Twttr", "Should remove vowels"

def test_capitalized_vowel_replacement():
    assert shorten("TWITTER") == "TWTTR", "Should remove capitalized vowels"

def test_lowercase_vowel_replacement():
    assert shorten("twitter") == "twttr", "Should remove lowercase vowels"

def test_omit_numbers():
    assert shorten("T3st1ng123") == "T3st1ng123", "Should not remove numbers"

def test_no_vowels():
    assert shorten("TWTTR") == "TWTTR", "Should return the same string when there are no vowels"

def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR", "Should handle mixed case vowels correctly"

def test_punctuation():
    assert shorten("Twi,tter!") == "Twttr!", "Should not remove punctuation"

# You can run these tests by executing pytest in the command line:
# pytest test_twttr.py
