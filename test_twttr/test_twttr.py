from twttr import shorten

# Vowel replacement
assert shorten("Twitter") == "Twttr"

# Capitalized vowel replacement
assert shorten("TWITTER") == "TWTTR"

# Lowercase vowel replacement
assert shorten("twitter") == "twttr"

# Omitting numbers
assert shorten("T3st1ng123") == "T3st1ng123"

# No vowels to remove
assert shorten("TWTTR") == "TWTTR"

# Mixed case
assert shorten("TwItTeR") == "TwtTR"

# Punctuation
assert shorten("Twi,tter!") == "Twttr!"

print("All tests passed!")
