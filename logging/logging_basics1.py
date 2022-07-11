
""" When importing 'employee' it's executing the code and
creates its 'employee.log' and then it creates the logging file
of this class - 'test.log';
Here we don't use the root logger, but our own
"""

import logging
import logging_basics2
""" Logging levels

- DEBUG: Detailed information, typically of interest only when diagnosing problems.
- INFO: Confirmation that things are working as expected.
- WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
- ERROR: Due to a more serious problem, the software has not been able to perform some function.
- CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

default logging level is WARNING
Log Record Attribute Docs: https://docs.python.org/3/library/logging.html#logrecord-attributes
"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.DEBUG) # we can capture specific levels
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# # basic/default configurationin using the root logger ('format' the separator is ':')
# logging.basicConfig(filename='test.log', level=logging.DEBUG,
# 					format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
	"""Add function"""
	return x + y

def subtract(x, y):
	"""Subtract function"""
	return x - y

def multiply(x, y):
	"""Multiply function"""
	return x * y

def divide(x, y):
	"""Divide function"""
	try:
		result = x / y
	except ZeroDivisionError:
		logger.exception('Tried to divide by zero')
	else:
		return result

num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.debug(f'Add: {num_1} + {num_2} = {add_result}')

sub_result = subtract(num_1, num_2)
logger.debug(f'Sub: {num_1} - {num_2} = {sub_result}')

mul_result = multiply(num_1, num_2)
logger.debug(f'Mul: {num_1} * {num_2} = {mul_result}')

div_result = divide(num_1, num_2)
logger.debug(f'Div: {num_1} / {num_2} = {div_result}')
