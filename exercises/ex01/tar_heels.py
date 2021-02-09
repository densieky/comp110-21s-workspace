"""An exercise in remainders and boolean logic."""
__author__ = "730322721"
# Begin your solution here...
an_integer: int = int(input("Enter an int: ")) 
if an_integer % 2 == 0 and an_integer % 7 != 0:
    print("TAR") 
if an_integer % 7 == 0 and an_integer % 2 != 0:
    print("HEELS")
if an_integer % 2 == 0 and an_integer % 7 == 0:
    print("TAR HEELS") 
if an_integer % 2 != 0 and an_integer % 7 != 0:
    print("CAROLINA") 