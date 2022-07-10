
class Employee:

	num_of_epms = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = '{}.{}@company.com'.format(first, last)

		Employee.num_of_epms += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	# usual methods work with instances, but with a decorator it's working with a class
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	# alternative/additional constructor expecially for this case
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	#
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
new_emp_1 = Employee.from_string(emp_str_1)

import datetime
my_date = datetime.date(2022, 7, 11)
print(Employee.is_workday(my_date))