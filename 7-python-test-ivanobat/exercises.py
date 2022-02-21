#
# 1)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}
#
# NOTE: Don't use any built-in functions!

def dictionary_maker(tuples_list):
    dictionary = {}
    for item in tuples_list:
        dictionary[item[0]] = item[1]
    print(dictionary)
    return dictionary

############################################
############################################
#
# You are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'foo', 'jobs': ['bar', 'baz', 'qux']}
#
# we will refer to this as a "CV".
#
############################################
############################################



#
# 2)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.
def has_experience_as(cv_list, job_title):
    users_with_experience = []
    for cv in cv_list:
        for job in cv['jobs']:
            if job == job_title:
                users_with_experience.append(cv['user'])
    print(users_with_experience)
    return users_with_experience

#
# 3)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.

def job_counts(cv_list):
    job_count = {}
    for cv in cv_list:
        jobs = cv['jobs'] 
        for job in jobs:  
            if job in job_count:
                job_count[job] = job_count.get(job,0) + 1
            else:
                job_count[job] = 1
    return job_count

#
# 4)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.

def most_popular_job(cv_list):
    highest_count = 0
    job_count = job_counts(cv_list)
    for k,v in job_count.items():
        if v >= highest_count:
            most_popular_job = (k, v)
            highest_count = v
    return most_popular_job

############################################
############################################
# Scoreboard
#
# In this part we will pretend
# we have an imaginary arcade
# game and we need to keep track
# of users and their scores on
# each level.
#
# You will create:
# 1. A class "User" with some methods.
# 2. Some separate functions that
#    use the User class.
#
############################################
############################################


#
# 5)
# Create a class called "User"
#
# The class should be instantiated
# with one attribute: "name"
# which is a string.
#
class User():
    def __init__(self, name):
        self.name = name
        self.scores = {}
        return None

#
# 6)
# Add methods "add_score" and
# "get_scores" to the User class.
#
    def add_score(self, level, score):
         
        if score<0 or not isinstance(score, int):
            raise ValueError('Invalid score')
        if level in self.scores:
            self.scores[level].append(score)
        else:
            self.scores[level] = [score]
        self.scores['name'] = self.name 
        return self.scores

# "add_score" should store the user's
# score for a given level. The choice
# of how to store it is up to you,
# but each user can have multiple
# scores for each level.
#
# "add_score" should have parameters:
# 1. level (str)
# 2. score (int)
# and should return nothing.
#
# "get_scores" should have one parameter:
# 1. level (str)
# and should return a list of integers
# representing the scores the user
# has achieved for that level
#
    def get_scores(self, level):
        for item in self.scores:
            if level in self.scores and self.scores['name'] == self.name:
                return self.scores[level]
            else:
                return None

#
# 7)
# Modify the "add_score" method
# so that it throws an error if the
# "score" it is given is not an integer
# or is negative.
#
#
#
# 8)
# Create a "top_score" method
# that has one parameter: "level"
# and returns the user's top score
# for that level.
#
# If the user has no score for that
# level, the method should return None

    def top_score(self, level):
        highest = 0
        for item in self.scores:
            scores = self.get_scores(level)
            if scores is None:
                highest = None
            else:
                for score in scores:
                    if score >= highest:
                        highest = score
        return highest

    def get_levels(self):
        levels = []
        levels_distinct = []
        for item in self.scores.keys():
            if item != 'name':
                levels.append(item)
        return levels
# 9)
# Now create a separate function
# called "top_player" that has two
# parameters:
# 1. a list of User objects
# 2. a level (str)
#
# And returns a tuple with the following
# form: (str, int) where the values
# represent: (player_name, score)

def top_player(user_list, level):
    highest_score = 0
    for player in user_list:
        if player.top_score(level) is None:
            return None
        elif player.top_score(level) >= highest_score:
            highest_score = player.top_score(level)
            top_player = (player.name, highest_score)      
    return top_player
    
#
# 10)
# Now modify the function "top_player"
# so that it returns None if given a level
# that no player has played


#
# 11)
# Create a separate function
# called "best_scores".
#
# This function should have one
# parameter: a list of User objects
# and should return a list of tuples
# of the following form:
# (str, str, int)
# where the values represent:
# (level, player_name, score)
#
# The list should be sorted with
# the top score coming first
# and should be truncated to the
# top 3 scores.
#
# HINT: use the builtin "sorted"
# function to sort a list and
# look how to use key-functions:
# https://docs.python.org/3/howto/sorting.html

def best_scores(user_list):
    best_scores = []
    for player in user_list:
        levels = player.get_levels()
        for level in levels:
            best_scores.append((level,player.name, player.top_score(level)))
            
    best_scores = sorted(best_scores, key=lambda scores: scores[2], reverse = True)
    return best_scores[:3]