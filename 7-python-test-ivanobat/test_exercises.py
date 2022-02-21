from exercises import *
import pytest


def test_dictionary_maker():
    li = [('foo', 1), ('bar', 3)]
    assert dictionary_maker(li) == {'foo': 1, 'bar': 3}

    li = []
    assert dictionary_maker(li) == {}


def test_has_experience_as():
    cvs = [{'user': 'foo', 'jobs': ['data monkey', 'copyist', 'wrecking ball operator']},
           {'user': 'bar', 'jobs': ['wrecking ball operator', 'poet']},
           {'user': 'baz', 'jobs': ['dancer', 'waitstaff']},
           {'user': 'qux', 'jobs': ['wrecking ball operator']}]

    assert has_experience_as(cvs, 'dancer') == ['baz']
    assert has_experience_as(cvs, 'poet') == ['bar']

    wreckers = has_experience_as(cvs, 'wrecking ball operator')
    assert len(wreckers) == 3
    for user in ['bar', 'foo', 'qux']:
        assert user in wreckers

def test_job_counts():
    cvs = [{'user': 'foo', 'jobs': ['data monkey', 'copyist', 'wrecking ball operator']},
           {'user': 'bar', 'jobs': ['wrecking ball operator', 'poet']},
           {'user': 'baz', 'jobs': ['dancer', 'waitstaff']},
           {'user': 'qux', 'jobs': ['wrecking ball operator', 'waitstaff']}]

    assert job_counts(cvs) == { 'dancer': 1,
                                'waitstaff': 2,
                                'wrecking ball operator': 3,
                                'copyist': 1,
                                'poet': 1,
                                'data monkey': 1}


def test_most_popular_job():
    cvs = [{'user': 'foo', 'jobs': ['data monkey', 'copyist', 'wrecking ball operator']},
           {'user': 'bar', 'jobs': ['wrecking ball operator', 'poet']},
           {'user': 'baz', 'jobs': ['dancer', 'waitstaff']},
           {'user': 'qux', 'jobs': ['wrecking ball operator']}]

    assert most_popular_job(cvs) == ('wrecking ball operator', 3)




def test_user_class_has_name():
    user = User('foo')
    assert user.name == 'foo'


def test_user_add_and_get_multiple_scores():
    user = User('foo')
    user.add_score('bar', 100)
    user.add_score('bar', 250)
    scores = user.get_scores('bar')
    assert len(scores) == 2
    assert 100 in scores
    assert 250 in scores


def test_user_add_score_raises():
    user = User('foo')

    with pytest.raises(Exception):
        user.add_score('bar', -10)

def test_top_score():
    user = User('foo')
    user.add_score('bar', 100)
    user.add_score('bar', 250)
    assert user.top_score('bar') == 250
    assert user.top_score('baz') is None

def test_top_player():
    dat = [('foo', [('Koopa Troopa Beach', 500),
                    ('Rainbow Road', 100)]),
           ('bar', [('Koopa Troopa Beach', 300),
                    ('Rainbow Road', 700)])]

    users = [User(n) for n, _ in dat]
    for u, (_, scores) in zip(users, dat):
        for lvl, score in scores:
            u.add_score(lvl, score)

    player = top_player(users, 'Rainbow Road')
    assert player == ('bar', 700)

    player = top_player(users, 'Koopa Troopa Beach')
    assert player == ('foo', 500)

def test_top_player_when_none():
    dat = [('foo', [('Koopa Troopa Beach', 500),
                    ('Rainbow Road', 100)]),
           ('bar', [('Koopa Troopa Beach', 300),
                    ('Rainbow Road', 700)])]

    users = [User(n) for n, _ in dat]
    for u, (_, scores) in zip(users, dat):
        for lvl, score in scores:
            u.add_score(lvl, score)

    player = top_player(users, 'Not a level')
    assert player is None

def test_best_scores():
    dat = [('foo', [('Koopa Troopa Beach', 500)]),
           ('bar', [('Koopa Troopa Beach', 300),
                    ('Rainbow Road', 700)]),
           ('baz', [('Banshee Boardwalk', 1200),
                    ('Rainbow Road', 100),
                    ('Rainbow Road', 900)])]

    users = [User(n) for n, _ in dat]
    for u, (_, scores) in zip(users, dat):
        for lvl, score in scores:
            u.add_score(lvl, score)

    scores = best_scores(users)
    assert scores == [('Banshee Boardwalk', 'baz', 1200),
                           ('Rainbow Road', 'baz', 900),
                           ('Rainbow Road', 'bar', 700)]
