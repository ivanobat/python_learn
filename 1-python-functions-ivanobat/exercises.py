#
# Your can take a look at the tests
# in "test_exercises", but do not need to
# change anything there.
#
# To run the tests, you will need to install
# a couple of python libraries. You can
# install this by running:
# "python3 -m pip install -U --user pytest pytest-xdist".
# Once you have it installed:
# You can run the tests with:
# "pytest -f --color=yes --looponfail"
# from the terminal, inside this folder.

#
# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#
def triple(x):
	return x*3
#
# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#
def subtract(x, y):
	return x-y
#
# 3)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted, it returns None.
#
def safe_subtract(x, y):
	try:
		return x-y		
	except:
		return None

#
# 4)
# Create a function named "greet_person". It should
# accept a string as an argument and return that
# string as part of a longer sentence that says hello:
# i.e. "Sophia" --> "Hello, Sophia!"
# If the function is called with an argument that is
# not a string, it should return "Please provide a name."
# i.e. 5 --> "Please provide a name."
#
def greet_person(personName):
	try:
		return "Hello, " + personName + "!"
	except:
		return "Please provide a name."