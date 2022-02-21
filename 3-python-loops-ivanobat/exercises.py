#
# 1)
# Write a function "only_adults" that
# takes as input a list of numbers and
# returns only those numbers >= 18

def only_adults(num_list):
    num_result_list = []
    [num_result_list.append(num) for num in num_list if num is not None and num >= 18]
    return num_result_list

#
# 2)
# Write a function "get_only_adults" that
# takes as input a list of numbers and
# returns only those numbers >= 18
# and removes any None values from the list

def get_only_adults(num_list):
    num_result_list = []
    only_adults_list = only_adults(num_list)
    [num_result_list.append(num) for num in only_adults_list]
    return num_result_list

#
# 3)
# Write a function "are_all_adults" that
# takes as input a list of numbers
# and returns True if they are all >= 18,
# and returns False otherwise
# Is this a map, filter, or reduce?

def are_all_adults(num_list):
    return all([num>=18 for num in num_list])
    #return len(num_list) == len(only_adults(num_list))
    
#
# 4)
# Write a function "count_nones" that
# takes as input a list of any type of element
# and returns a count of how many of those
# elements are None types.
# Is this a map, filter, or reduce?
def count_nones(any_list):
    count = 0
    for item in any_list: 
        if item is None:
            count += 1
    return count

#
# 5)
# Write a function "longest_word" that
# takes as input a list of strings
# and returns the longest string in the
# list.
# Hint: you will need to use two "accumulators"

def longest_word(string_list):
    #lengths =[]
    #[lengths.append(len(item)) for item in string_list]
    #return string_list[lengths.index(max(lengths))]
    longest_length = 0
    for word in string_list:
        if len(word) > longest_length:
            longest_length = len(word)
            longest_word = word
    return longest_word
        
#
# 6)
# Write a function "factorial"
#
# It takes a number and returns the
# factorial of that number.
#
# The factorial of n is the product of all
# positive integers less than or equal to n
#
# HINT: use range()
# https://docs.python.org/3/library/stdtypes.html#typesseq-range
#
# range(n) produces an iterable of length n:
# [0,1,2,...,n-1]

def factorial(num):
    result = num
    factorial_list = [number+1 for number in range(num-1)]
    for number in factorial_list:
        result = result * number
    return result

# alternative with recursions
# def factorial(n):
#     if not isinstance(n,int) or n<0:
#         raise Exception('factorial only defined for non-negative integers')
#     if n == 0: return 1
#     elif n == 1: return 1
#     else: return n*factorial(n-1)
#
# 7)
# Write a function "second_highest_number"
# that takes as input a list of numbers
# and returns the second highest. Assume
# that the numbers will be unique (no duplicates).
#
# NOTE: Only use the operations and functions
# we have learned so far! No cheating!
#
# HINT: You might want to write two functions!
def highest_number(num_list):
    highest_num=0
    for num1 in num_list:
        for num2 in num_list:
            if num1>=num2 and num1>=highest_num:
                highest_num = num1
    return highest_num

def second_highest_number(num_list):
    highest_num=highest_number(num_list)
    num_list.remove(highest_num)
    return highest_number(num_list) 



#####################################################
# BONUS EXERCISES
# Uncomment the commented-out tests in test_exercises.py
# to unlock the bonus exercises.
#####################################################


# 8)
# Write a function "n_highest_number"
# with two parameters:
# 1. a list of numbers
# 2. an integer
#
# "n_highest_number" should return the nth
# highest number in the list, where n is the
# second parameter of the function. Assume
# that the numbers will be unique (no duplicates).
# Also assume that n <= the number of elements
# in the list.
#
# NOTE: Only use the operations and functions
# we have learned so far! No cheating!
#
# HINT: Can you reuse anything from the previous
# exercise? That may or may not work, depending
# on how you implemented it.
#
# HINT HINT: use the function "range"!
def n_highest_number(num_list, n):
    highest_num = 0
    count = 1
    temp_list = list(num_list)
    while count<=n:
        highest_num = highest_number(temp_list)
        temp_list.remove(highest_num)
        count += 1
    return highest_num

n_highest_number([10,5,3,8,1,2], 1)
#
# 9)
# Write a function "every" that
# takes two parameters:
# 1. a list of elements of data type E
# 2. a predicate function (E) -> bool. In
# other words, a function that has a single
# parameter, which is the same type as the
# elements of the list, and returns a boolean.
#
# "every" should return True if the predicate
# evaluates to true for every element in the list.
# Otherwise, it returns False.
#
# NOTE: we haven't yet seen functions
# passed as arguments, so this might
# feel strange. But it works!

def every(any_list, any_function):
    flag = True
    for item in any_list:
        if any_function(item) == False:
            flag = False
            break
        else:
            flag = True
    return flag        
    #return all([any_function(item) for item in any_list])
