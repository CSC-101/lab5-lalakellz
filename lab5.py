import data

# Write your functions for each part in the space below.

# Part 1

# Part 2

# Part 3
from typing import Any
class Time:
    #initialize new time object
    #input: hour as int
    #input: minute as int
    #input: second as int
    def __init__(self, hour : int, minute: int, second: int):
        self.hour = hour
        self. minute = minute
        self.second = second

    #Provide a developer-friendly string representation of the object
    #Input: self, time object where str is desired
    #outpu: a str representation
    def __repr__(self) -> str:
        return 'Time({}, {}, {})'.format(self.hour, self.minute, self.second)

    #compare time with another value to see equality
    # input: self time object to compare
    # input: other another value to compare to the Time
    # output: bool indicating equality
    def __eq__(self, other: Any) -> bool:
        return(other is self or (type(other) == Time and self.hour == other.hour and
                                 self.minute == other.minute and self.second == other.second))
"""
did i have to do all of the above?
it didnt say to but in the tasks before we did, but i think it would work the same without
"""
# Add two Time objects and return a new Time object representing their sum.
# input: time1 (a Time object to add)
# input: time2 (another Time object to add)
# output: a new Time object with the summed hour, minute, and second attributes
def time_add(time1: Time, time2: Time) -> Time:
    #sum of hors, minutes, seconds
    new_hr = time1.hour + time2.hour
    new_min = time1.minute + time2.minute
    new_sec = time1.second + time2.second

    # Adjust seconds to remain within 0–59 by carrying over to minutes
    if new_sec >= 60:
        new_min += new_sec // 60
        new_sec = new_sec % 60

    # Adjust minutes to remain within 0–59 by carrying over to hours
    if new_min >= 60:
        new_hr += new_min // 60
        new_min = new_min % 60

    #return sum
    return Time(new_hr, new_min, new_sec)

# Part 4
# Check if a list of floats is in descending order
# input: numbers, a list of floats
# output: bool
def is_descending(nums: list[float]) -> bool:
    #compares lists elements with the previous
    for i in range(1, len(nums)):
        #returns false if an element isnt less than the previous
        if nums[i] >= nums[i-1]:
            return False
    # if all elements r descending, return true
    return True

# Part 5


# Part 6
