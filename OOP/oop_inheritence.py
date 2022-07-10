
class Employee:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = '{}.{}@company.com'.format(first, last)

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
	""" by changing the variable value in subclass 
	it doesn't have any affect on other Employee instances """
	raise_amt = 1.10

	# when we want our subclass to have more arguments
	def __init__(self, first, last, pay, prog_lang):
		# Employee handles these arguments ( Employee.__init__(self, first, last, pay) ) 
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)

		if Employee is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
			
	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

dev_1 = Developer('Corey1', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test1', 'Employee', 60000, 'Java')
# print(help(Developer))
print(dev_1.email)
print(dev_2.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

dev_3 = Developer('Corey2', 'Schafer', 50000, 'Python')
dev_4 = Developer('Test2', 'Employee', 60000, 'Java')
print(dev_3.prog_lang)
print(dev_4.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_emps()
mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_3)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))