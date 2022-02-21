#
# 1)
# Create a function called "should_work"
# it should take one parameter: "tired"
# which is a boolean.
# if tired is True, should_work should return
# False. If tired is False, should_work should
# return True. (i.e. it returns the opposite)
#
def should_work(tired):
    if tired == True:
        return False
    else:
        return True


# 2)
# Create a function called "is_even"
# that takes one parameter: "num"
# which is a number.
# It returns True if the number is even
# and False if the number is odd.
# It should raise an error if not
# given a numer
#
def is_even(num):
    if type(num) != int:
        raise ValueError('This is not a number')
    return num%2 == 0

# 2)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception.
#
def car_at_light(light):
    if light == 'red':
        return 'stop'
    elif light == 'green':
        return 'go'
    elif light == 'yellow':
        return 'wait'
    else:
        raise ValueError()
#
# 3)
# Create a function called "is_cold"
# which takes one parameter: "temperature"
# which is a number.
# If the temperature is above 15 degrees,
# it should return False,
# if it is equal or below 15 degrees,
# it should return True,
# if the temperature is not a number,
# it should raise an exception that
# says "temperature must be a number"
# (hint: you need to raise an exception
# with EXACTLY that message)
def is_cold(temperature):
    if type(temperature) != int and type(temperature) != float:
        raise ValueError('temperature must be a number')
   
    return temperature <= 15
    
#
# 4)
# Create a function called "wear_sweater"
# which takes two parameter: "temperature", "friolera"
# The first is a number, the second a boolean
# (which might sometimes be a None).
# If the temperature is above 15,
# it should return False,
# if it is 15 or below,
# it should return True if friolera
# is True, False if friolera is False,
# and True if friolera is None.
# (In other words, if we don't know whether
# she is a friolera or not, we should act
# cautiously and tell her to wear a sweater)
# (hint: you should use is_cold from above!)
def wear_sweater(temperature, friolera):
    if is_cold(temperature) and friolera == True:
        return True
    elif friolera is None:
        print('Wear a sweater')
        return True
    else:
        return not is_cold(temperature) and friolera == False
#
# 5)
# Create a function called "equality"
# which takes three parameters: "x", "y", and "z"
# it should return the following:
# if x, y, and z are all equal --> "all are equal"
# if only x and y are equal --> "x and y are equal"
# if only z and x are equal --> "x and z are equal"
# if only y and z are equal --> "y and z are equal"
# if nothing is equal --> "nothing is equal"

def equality(x, y, z):
    if x == y and y == z:
        return 'all are equal'
    elif x == y and x != z:
        return 'x and y are equal'
    elif z == x and z != y:
        return 'x and z are equal'
    elif y == z and y != x:
        return 'y and z are equal'
    elif (x!=y or x is None) and (y!=z or y is None) and (z!=x or z is None):
        return 'nothing is equal'
    
# 6)
# Write a function for the following situation:
# Sofia can drive manual and automatic cars.
# Diego only knows how to drive automatic.
# Sofia prefers to drive long distances (> 10 km).
# Diego prefers to drive short distances.
#
# The function should be called "driver_seat"
# and should take two parameters: "distance", "is_manual".
# The first should be a number, the second should be a
# boolean. The function should return a string, which is
# the name of the person who should drive, "Diego" or "Sofia".

def driver_seat(distance, is_manual):
    if distance > 10 or is_manual == True:
        return 'Sofia'
    elif is_manual == False: 
        return 'Diego'
    else:
        return 'Sofia'
        