
class Employee:

	raise_amt = 1.04

	# dunder - surrounded by double underscores
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = '{}.{}@company.com'.format(first, last)

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	# for debagging and logging
	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

	# more readable representation
	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)

	# when we add two employees together, we add and return their salaries
	def __add__(self, other):
		return self.pay + other.pay

	# return the total number of the fullname
	def __len__(self):
		return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)
print(emp_1 + emp_2)

print(len(emp_1))

# how works addition for 'int' and 'str'
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

print(len('test'))
print('test'.__len__())