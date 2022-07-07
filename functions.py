
# DRY - don't repeat yourself
def blink_func():
	pass
print(blink_func())

def hello_func():
	return 'Hello Function.'
print(hello_func().upper())

def hi_func1(greeting):
	return '{} Function!'.format(greeting)
print(hi_func1('Hi'))

def hi_func2(greeting, name='You'):
	return '{}, {}!'.format(greeting, name)
print(hi_func2('Hi'))
print(hi_func2('Hi', name='Corey'))

# *args - positional arguments, *kwargs - keyword arguments
def student_info(*args, **kwargs):
	"""Doc string that explains what the function does"""

	print(args) # tuple
	print(kwargs) # dictionary
student_info('Math', 'CompSci', name='Corey', age=22)

courses = ['Math', 'Art']
info = {'name': 'Jane', 'age': 19}
student_info(*courses, **info)

# --- Exmaple of Functions ---

# Number of days per month. First value placehodler for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	"""Returns True for leap years, False for non-leap years."""

	return year % 4 == 0 and (year % 100 != 0 and year % 400 == 0)

def days_in_month(year, month):
	"""Returns number of days in that month in that year."""

	# year 2017
	# month 2
	if not 1 <= month <= 12:
		return 'Invalid Month'

	if month == 2 and is_leap(year):
		return 28

	return month_days[month]

print(days_in_month(2017, 2))