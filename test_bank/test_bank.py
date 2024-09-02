import pytest
from bank import value

# Test if the correct value is returned for various greetings
def test_correct_values():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello world") == 0
    assert value("hi") == 20
    assert value("Hi there") == 20
    assert value("hey") == 100
    assert value("greetings") == 100

# Test to catch incorrect values (negative test cases)
def test_incorrect_values():
    assert value("hello") != 20
    assert value("Hi there") != 100
    assert value("hey") != 20

# Test to ensure case-insensitivity
def test_case_insensitivity():
    assert value("Hello") == 0
    assert value("hELLo") == 0
    assert value("HeLLo") == 0
    assert value("HI") == 20
    assert value("hI") == 20

# Test to ensure entire phrase is considered
def test_entire_phrase():
    assert value("hello world") == 0
    assert value("HELLO there!") == 0
    assert value("hi everyone") == 20
    assert value("hELLo there, everyone!") == 0

# Test to activate only if all above tests pass
def test_activation():
    test_correct_values()
    test_incorrect_values()
    test_case_insensitivity()
    test_entire_phrase()

if __name__ == "__main__":
    pytest.main()
