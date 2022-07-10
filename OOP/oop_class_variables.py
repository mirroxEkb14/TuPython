
class Employee:

	""" class variables are the same for each instance
		    those are variables that are shared among all Employees """
	raise_amount = 1.04 # 4%
	num_of_epms = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = '{}.{}@company.com'.format(first, last)

		Employee.num_of_epms += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_epms)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(Employee.num_of_epms)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)