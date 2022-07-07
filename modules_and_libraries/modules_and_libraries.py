
import my_module as mm
courses = ['History', 'Math', 'Physics', 'CompSci']
index = mm.find_index(courses, 'Math')
print(index)

from my_module import find_index, test
print(find_index(courses, 'History'))
print(test)

import random
random_course = random.choice(courses)
print(random_course)

import math

import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

import os
print(os.getcwd()) # current working directory (where the current script is located)
print(os.__file__) # the location the module

import antigravity