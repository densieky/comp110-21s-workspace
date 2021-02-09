"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730322721"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...") 
your_message: int = randint(0, 100) 
if your_message > 75:
    print("Here comes the sun.") 
else:
    if your_message < 25:
        print("Something brand new is headed your way.")      
    else:
        if your_message > 50:
            print("People are waiting for you to be exactly who you are.")
        else: 
            print("It's alright.")
print("Now, go spread positive vibes!")