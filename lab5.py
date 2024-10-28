import math

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
from typing import List, Optional
# Find the index of the largest value in a list between two specified indexes.
# input: numbers (a list of integers to examine)
# input: lower (starting index of the range to search, inclusive)
# input: upper (ending index of the range to search, inclusive)
# output: integer (index of the largest value within the range), or None if the range is invalid or out of bounds
def largest_between(nums: List[int], lower: int, upper: int) -> Optional[int]:
    #checks if the range is invalid
    if lower > upper:
        return None

    # adjust bounds if out of range
    lower = max(0, lower)
    upper = min(len(nums) - 1, upper)

    # range still empty
    if lower > upper:
        return None

    #initialize the largest value and its index
    max_index = lower
    max_value = nums[lower]

    #loop through range to find max / its index
    for i in range(lower, upper +1):
        if nums[i] > max_value:
            max_value = nums[i]
            max_index = i
    return max_index

# Part 6
class Point:
    # Initialize a new Point object.
    # input: x-coordinate as a float
    # input: y-coordinate as a float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# Function to find the index of the point furthest from the origin in a list of Points.
# input: points (a list of Point objects)
# output: integer (index of the point furthest from origin), or None if list is empty
def furthest_from_origin(points: List[Point]) -> Optional[int]:
    #checks if empty
    if not points:
        return None

    max_distance = 0 #track  maximum distance
    max_index = 0 #track index of furthest point
    i = 0 # track the index in the list

    while i < len(points):
        #distance from the origin using the Euclidean distance formula
        distance = math.sqrt(points[i].x ** 2 + points[i].y ** 2)

        # Update max_distance and max_index if the current point's distance is greater
        if distance > max_distance:
            max_distance = distance
            max_index = i
        i += 1 # Move to the next index

    return max_index
