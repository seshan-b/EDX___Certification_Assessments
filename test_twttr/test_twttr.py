import pytest
from twttr import shorten

def test_vowel_replacement():
    assert shorten("Twitter") == "Twttr"

def test_capitalized_vowel_replacement():
    assert shorten("TWITTER") == "TWTTR"

def test_lowercase_vowel_replacement():
    assert shorten("twitter") == "twttr"

def test_omit_numbers():
    assert shorten("T3st1ng123") == "T3st1ng123"

def test_no_vowels():
    assert shorten("TWTTR") == "TWTTR"

def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"

def test_punctuation():
    assert shorten("Twi,tter!") == "Twttr!"
