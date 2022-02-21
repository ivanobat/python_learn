from exercises import *

def test_only_adults():
    ages = [1,15,30,35]
    res = only_adults(ages)
    assert res == [30,35]

    ages = [30,35]
    res = only_adults(ages)
    assert res == [30,35]

def test_get_only_adults():
    ages = [1,15,None,30,None,35]
    res = get_only_adults(ages)
    assert res == [30,35]

    ages = [30,35]
    res = get_only_adults(ages)
    assert res == [30,35]


def test_are_all_adults():
    ages = [1,15,30,35]
    res = are_all_adults(ages)
    assert res == False

    ages = [35,1,15]
    res = are_all_adults(ages)
    assert res == False

    ages = [30,35]
    res = are_all_adults(ages)
    assert res == True

def test_count_nones():
    ages = [1,15,None,30,None,35]
    assert count_nones(ages) == 2

    ages = [1,15,30,35]
    assert count_nones(ages) == 0

def test_longest_word():
    words = ['foo', 'foobar', 'foobarbaz']
    assert longest_word(words) == 'foobarbaz'

    words = ['foo', 'foobarbaz', 'foobar']
    assert longest_word(words) == 'foobarbaz'

    words = ['foo']
    assert longest_word(words) == 'foo'

def test_factorial():
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(12) == 479001600

def test_second_highest_number():
    nums = [10,5,3,8]
    assert second_highest_number(nums) == 8

    nums = [1,2]
    assert second_highest_number(nums) == 1


def test_n_highest_number():
    nums = [10,5,3,8,1,2]
    assert n_highest_number(nums, 2) == 8
    assert n_highest_number(nums, 1) == 10
    assert n_highest_number(nums, 3) == 5
    assert n_highest_number(nums, 6) == 1


def test_every():
    def is_adult(n):
        return n >= 18

    assert every([10, 17, 30], is_adult) == False
    assert every([35, 30], is_adult) == True

    def is_long(s):
        return len(s) > 3

    assert every(['fo', 'foobar'], is_long) == False
    assert every(['foooo', 'bar'], is_long) == False
    assert every(['fooo', 'barrr'], is_long) == True
