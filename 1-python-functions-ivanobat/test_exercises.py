from exercises import *

def test_triple():
    assert triple(5) == 15
    assert triple(10) == 30

def test_subtract():
    assert subtract(1, 1) == 0
    assert subtract(10, 3) == 7

def test_safe_subtract():
    assert safe_subtract(1, 1) == 0
    assert safe_subtract(10, 3) == 7
    assert safe_subtract(None, 5) is None
    assert safe_subtract("10", 2) is None

def test_greet_person():
    assert greet_person('Sophia') == 'Hello, Sophia!'
    assert greet_person(10) == 'Please provide a name.'
    assert greet_person(None) == 'Please provide a name.'