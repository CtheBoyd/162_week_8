# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date:7/28/2022
# Description: Sorting functions with timer that counts the time it takes a function to run.
#

import time
import random
from functools import wraps

def sort_timer(func):
    """adds a timer around a sort function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        stop = time.perf_counter()
        stopwatch = stop - start
        return stopwatch
    return wrapper

@sort_timer
def bubble_sort(a_list):
    """ Sorts a_list in ascending order"""

    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp

@sort_timer
def insertion_sort(a_list):
    """Sorts a_list in ascending order"""

    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value

@sort_timer
def compare_sorts(bubble_sort, insertion_sort):
    """function called compare_sorts that takes the two decorated sort functions as parameters.
    Randomly generate a list of 1000 numbers and then make a separate copy of that list
    Compares the sort functions and returns a graph of the time each sort function returns"""
    x_val = []
    y_val_1 = []
    y_val_2 = []
    for size in range(1000, 10001, 1000):
        nums = [random.randint(1, 10000) for i in range(size)]
        copy = list(nums)
        print(size)
        time_1 = bubble_sort(nums)
        time_2 = insertion_sort(copy)
        x_val.append(size)
        y_val_1.append(time_1)
        y_val_2.append(time_2)

    from matplotlib import pyplot
    pyplot.plot(x_val, y_val_1, 'ro--', linewidth=2, label='bubble_sort')
    pyplot.plot(x_val, y_val_2, 'go--', linewidth=2, label='insertion_sort')
    pyplot.xlabel("Array size")
    pyplot.ylabel("Time")
    pyplot.legend(loc='upper left')
    pyplot.show()




compare_sorts(bubble_sort, insertion_sort)
