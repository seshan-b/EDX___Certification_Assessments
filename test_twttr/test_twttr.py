import subprocess

def test_basic_vowel_removal():
    assert shorten("Twitter") == "Twttr", "Failed to remove vowels from 'Twitter'"

def test_capitalized_vowel_removal():
    assert shorten("TWITTER") == "TWTTR", "Failed to remove capitalized vowels from 'TWITTER'"

def test_lowercase_vowel_removal():
    assert shorten("twitter") == "twttr", "Failed to remove lowercase vowels from 'twitter'"

def test_mixed_case_vowel_removal():
    assert shorten("TwItTeR") == "TwtTR", "Failed to handle mixed case vowels in 'TwItTeR'"

def test_number_handling():
    assert shorten("T3st1ng123") == "T3st1ng123", "Numbers should not be removed"

def test_no_vowels():
    assert shorten("TWTTR") == "TWTTR", "String with no vowels should remain unchanged"

# def test_punctuation_handling():
#     # Running the script through subprocess to check the exit code
#     result = subprocess.run(["python3", "twttr.py"], input="Twi,tter!", text=True, capture_output=True)
#     assert result.returncode == 1, "Expected exit code 1, but got 0"
#     assert "Error: Punctuation mishandled" in result.stdout, "Expected error message not found"

if __name__ == "__main__":
    test_basic_vowel_removal()
    test_capitalized_vowel_removal()
    test_lowercase_vowel_removal()
    test_mixed_case_vowel_removal()
    test_number_handling()
    test_no_vowels()
    # test_punctuation_handling()
    print("All tests passed!")
