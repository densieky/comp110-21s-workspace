"""A vaccination calculator."""

__author__ = "730322721"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

pop: int = int(input("Population: "))

doses_admin: int = int(input("Doses Administered: "))

doses_per_day: int = int(input("Doses Per Day: "))

tgt_vac: int = int(input("Target % Vaccinated: "))
number_of_days: int = round((((tgt_vac * pop) / 100) - (doses_admin / 2)) / (doses_per_day / 2))
until: timedelta = timedelta(number_of_days)
today: datetime = datetime.today()
day_of: datetime = today + until
str_day: str = day_of.strftime("%B %d, %Y")
print("We will reach " + str(tgt_vac) + "% vaccination in " + str(until) + ", which falls on " + str_day + ".") 