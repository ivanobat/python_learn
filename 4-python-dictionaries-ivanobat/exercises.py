#
# INSTRUCTIONS:
# For this exercise we will work with a
# "scoreboard" for an imaginary game.
# You will be required to write functions
# that operate on the "scoreboard" data
# structure and compute certain results.



######################################
# TUPLES
#
# For these functions, the "scoreboard"
# will be a list of tuples, where each
# tuple is of the form (str, int)
# representing (player_name, score)
#
# For example:
# [('kewld00d1', 100), ('pumpkin', 550)]
######################################


#
# 1)
# Create a function "get_scores"
# that has one parameter, the scoreboard,
# and returns a list of the same size
# with just the scores for each player
# (a list of ints)
def get_scores(scoreboard):
    scores = []
    [scores.append(score) for player_name, score in scoreboard]
    return scores    
#
# 2)
# Create a function "top_score"
# that has one parameter, the scoreboard,
# and returns an int, the highest score
# on the scoreboard

def top_score(scoreboard):
    highest = 0
    counter = 1
    nth_highest = 1
    for player_name, score in scoreboard:
        if score >= highest:
            highest = score
    return highest
#
# 3)
# Create a function "top_player"
# that has one parameter, the scoreboard,
# and returns the player_name that has
# the highest score
def top_player(scoreboard):
    for player_name, score in scoreboard:
        if score == top_score(scoreboard):
            return player_name

######################################
# DICTIONARIES
#
# For these functions, the "scoreboard"
# will be a list of dictionaries, where each
# dictionary represents information
# about a single player.
#
# The keys of the dictionary are:
# "player", "score", "country", "levels"
#
# For example, one dictionary:
#
# {
#    'player': 'tr0llhuntah',
#    'score': 200,
#    'country': 'no',
#    'levels': ['Choco Mountain', 'Rainbow Road']
# }
#
######################################


#
# 4)
# Create a function "top_player_from_dict"
# that has one parameter, the scoreboard,
# and returns the player_name that has
# the highest score
def top_player_from_dict(scoreboard):
    highest_player = None
    highest = 0
    for item in scoreboard:
        if item['score'] >= highest:
            highest = item['score']
            highest_player = item['player']
    return highest_player
#
# 5)
# Create a function "get_good_players"
# that has two parameters:
# 1. scoreboard
# 2. an int (limit)
#
# "get_good_players" returns a list of
# strings, with the names of the players
# who have a score greater than or equal to
# limit.
def get_good_players(scoreboard, limit):
    good_players=[]
    #good_players.append( [item['player'] for item in scoreboard if item['score']>=limit])
    for item in scoreboard:
        if item['score']>=limit:
            good_players.append(item['player'])
    return good_players

#
# 6)
# Create a function "top_player_by_country"
# that has two parameters:
# 1. scoreboard
# 2. a string (country)
#
# "top_player_by_country" returns a string
# with the name of the player with the highest
# score in the provided country.
def top_player_by_country(scoreboard, country):
    top_by_country = None
    scoreboard_by_country = {}
    scoreboard_by_country  = [item for item in scoreboard if item['country'] == country]
    top_by_country = top_player_from_dict(scoreboard_by_country)
    return top_by_country
#
# 7)
# Create a function "most_levels_played"
# that has one parameter: "scoreboard".
# and returns a tuple (str, int) with the name of
# the player that has played the most levels
# and the number of levels they played


def most_levels_played(scoreboard):
    highest_levels = 0
    top_player_levels = ()
    scoreboard_with_count = [(item['player'], len(item['levels'])) for item in scoreboard]
    for item in scoreboard_with_count:
        if item[1]>=highest_levels:
            top_player_levels = item
            highest_levels = item[1]
    return top_player_levels

#
# 8)
# Create a function "played_levels"
# that has one parameter: "scoreboard".
# and returns a list of strings with the
# names of all the levels that have been
# played by any user.
#
# The list of levels can have duplicates.

def played_levels(scoreboard):
    all_levels = []
    temp_levels = [(item['levels']) for item in scoreboard]
    for item1 in temp_levels:
        for item2 in item1:
            all_levels.append(item2)
    return all_levels

######################################
# BONUS QUESTIONS
######################################

#
# 9)
# Create a function "distinct" that
# takes a list of elements and returns
# a list of only the unique elements.
#
# Example:
# [1,2,2,2,1,3] -> [1,2,3]
#
# NOTE: Use only the tools we have learned
# so far:
# dictionaries, lists, for loop, try/except

def distinct(any_list):
    distinct_list = []
    #distinct_list.append([item for item in any_list if item not in distinct_list])
    for item in any_list:
        if item not in distinct_list:
            distinct_list.append(item)
    return distinct_list

#
# 10)
# Create a function "distinct_played_levels"
# That is just like "played_levels" except
# that it returns a list of the unique
# levels played (a list without duplicates)
#
# HINT: just use the two functions you've
# already written!

def distinct_played_levels(scoreboard):
    return distinct(played_levels(scoreboard))

#
# 11)
# Modify your function "top_player_by_country":
#
# Now, the second parameter ("country") should
# be either the country code OR None. If it
# is None, the function should return the top
# player across all countries
def top_player_by_country(scoreboard, country):
    top_by_country = None
    scoreboard_by_country = {}
    scoreboard_by_country  = [item for item in scoreboard if item['country'] == country or country is None]
    top_by_country = top_player_from_dict(scoreboard_by_country)
    return top_by_country

# 12)
# Create a function called "country_leaderboard"
#
# This function will return a "leaderboard" that
# provides information about the top player
# per country.
#
# The "leaderboard" should be a dictionary.
# See the test_exercises.py file for the format.

def country_leaderboard(scoreboard):
    leaderboard = {}
    leaderboard2 = {}
    countries = distinct([item['country'] for item in scoreboard])
    for country in countries:
        #leaderboard2[country] = {'player':item['player'],'score':item['score'] for item in scoreboard if top_player_by_country(scoreboard, country) == item['player']}
        for item in scoreboard:
            if top_player_by_country(scoreboard, country) == item['player']:
                leaderboard[country] = {'player':item['player'],'score':item['score']}
    print(leaderboard)
    #del leaderboard['country']
    return leaderboard
    
scoreboard =[{ 'player': 'kewld00d1', 'score': 100, 'country': 'gr'},
                      { 'player': 'pumpkin', 'score': 550, 'country': 'gr'},
                      { 'player': 'tr0llhuntah', 'score': 200, 'country': 'no'},
                      { 'player': '111111', 'score': 50, 'country': 'no'}]

country_leaderboard(scoreboard)