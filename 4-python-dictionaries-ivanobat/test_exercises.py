from exercises import *

def test_get_scores():
    scoreboard = [('kewld00d1', 100), ('pumpkin', 550), ('tr0llhuntah', 200)]
    assert get_scores(scoreboard) == [100, 550, 200]

def test_top_score():
    scoreboard = [('kewld00d1', 100), ('pumpkin', 550), ('tr0llhuntah', 200)]
    assert top_score(scoreboard) == 550

def test_top_player():
    scoreboard = [('kewld00d1', 100), ('pumpkin', 550), ('tr0llhuntah', 200)]
    assert top_player(scoreboard) == 'pumpkin'

def test_top_player_from_dict():
    scoreboard = [{ 'player': 'kewld00d1', 'score': 100},
                  { 'player': 'pumpkin', 'score': 550},
                  { 'player': 'tr0llhuntah', 'score': 200}]

    assert top_player_from_dict(scoreboard) == 'pumpkin'

def test_get_good_players():
    scoreboard = [{ 'player': 'kewld00d1', 'score': 100},
                  { 'player': 'pumpkin', 'score': 550},
                  { 'player': 'tr0llhuntah', 'score': 200}]

    assert get_good_players(scoreboard, 500) == ['pumpkin']
    assert get_good_players(scoreboard, 200) == ['pumpkin', 'tr0llhuntah']


def test_top_player_by_country():
    scoreboard = [{ 'player': 'kewld00d1', 'score': 100, 'country': 'gr'},
                  { 'player': 'pumpkin', 'score': 550, 'country': 'gr'},
                  { 'player': 'tr0llhuntah', 'score': 200, 'country': 'no'},
                  { 'player': '111111', 'score': 50, 'country': 'no'}]

    assert top_player_by_country(scoreboard, 'no') == 'tr0llhuntah'
    assert top_player_by_country(scoreboard, 'gr') == 'pumpkin'


def test_most_levels_played():
    scoreboard = [{ 'player': 'kewld00d1', 'levels': ['Koopa Troopa Beach']},
                  { 'player': 'pumpkin', 'levels': ['Choco Mountain', 'Rainbow Road']},
                  { 'player': 'tr0llhuntah', 'levels': ['Banshee Boardwalk']}]

    assert most_levels_played(scoreboard) == ('pumpkin', 2)


def test_played_levels():
    scoreboard = [{ 'player': 'kewld00d1', 'levels': ['Koopa Troopa Beach']},
                  { 'player': 'pumpkin', 'levels': ['Choco Mountain', 'Rainbow Road']},
                  { 'player': 'tr0llhuntah', 'levels': ['Banshee Boardwalk']}]

    assert played_levels(scoreboard) == ['Koopa Troopa Beach', 'Choco Mountain', 'Rainbow Road', 'Banshee Boardwalk']


def test_distinct():
    assert distinct([1,2,2,2,3]) == [1,2,3]
    assert distinct(['foo', 'foo', 'bar']) == ['foo', 'bar']


def test_distinct_played_levels():
    scoreboard = [{ 'player': 'kewld00d1', 'levels': ['Koopa Troopa Beach']},
                  { 'player': 'pumpkin', 'levels': ['Choco Mountain', 'Rainbow Road', 'Koopa Troopa Beach']},
                  { 'player': 'tr0llhuntah', 'levels': ['Choco Mountain', 'Banshee Boardwalk']}]

    assert distinct_played_levels(scoreboard) == ['Koopa Troopa Beach', 'Choco Mountain', 'Rainbow Road', 'Banshee Boardwalk']


def test_top_player_by_country_accepts_none():
    scoreboard = [{ 'player': 'kewld00d1', 'score': 100, 'country': 'gr'},
                  { 'player': 'pumpkin', 'score': 550, 'country': 'gr'},
                  { 'player': 'tr0llhuntah', 'score': 200, 'country': 'no'},
                  { 'player': '111111', 'score': 50, 'country': 'no'}]

    assert top_player_by_country(scoreboard, None) == 'pumpkin'

def test_country_leaderboard():
    scoreboard = [{ 'player': 'kewld00d1', 'score': 100, 'country': 'gr'},
                  { 'player': 'pumpkin', 'score': 550, 'country': 'gr'},
                  { 'player': 'tr0llhuntah', 'score': 200, 'country': 'no'},
                  { 'player': '111111', 'score': 50, 'country': 'no'}]

    assert country_leaderboard(scoreboard) == {'gr': {'player': 'pumpkin',
                                                      'score': 550},
                                               'no': {'player': 'tr0llhuntah',
                                                      'score': 200}}
