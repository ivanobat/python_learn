import pytest
from exercises import * 

def test_should_work():
    assert should_work(True) is False
    assert should_work(False) is True
    assert should_work(None) is True

def test_is_even():
    assert is_even(10) is True
    assert is_even(11) is False
    with pytest.raises(Exception) as e:
        assert is_even(None)        

def test_car_at_light():
    assert car_at_light("green") == "go"
    assert car_at_light("yellow") == "wait"
    assert car_at_light("red") == "stop"
    with pytest.raises(Exception) as e:
        assert car_at_light("foo")

def test_is_cold():
    assert is_cold(15) is True
    assert is_cold(20) is False
    with pytest.raises(Exception) as e:
        assert is_cold(None)
    assert str(e.value) == 'temperature must be a number'

def test_wear_sweater():
    assert wear_sweater(15, False) is False
    assert wear_sweater(15, True) is True
    assert wear_sweater(16, True) is False
    assert wear_sweater(15, None) is True
    with pytest.raises(Exception) as e:
        assert wear_sweater('foo', None)
    assert str(e.value) == 'temperature must be a number'

def test_equality():
    assert equality(10, 10, 10) == 'all are equal'
    assert equality(10, 10, 5) == 'x and y are equal'
    assert equality(10, 5, 10) == 'x and z are equal'
    assert equality(5, 10, 10) == 'y and z are equal'
    assert equality(5, 10, 15) == 'nothing is equal'

def test_driver_seat():
    assert driver_seat(15, True) == 'Sofia'
    assert driver_seat(15, False) == 'Sofia'
    assert driver_seat(10, True) == 'Sofia'
    assert driver_seat(10, False) == 'Diego'

