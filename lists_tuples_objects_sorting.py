
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li, reverse=True) # returns a new list, the original one remains the same
print('Sorted Variable:\t', s_li)
li.sort() # the original list changes
print('Original Variable:\t', li)

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup) # tuples do not have a 'sort' method
print('Tuple:\t', s_tup)

# the 'key' parameter runs each element through the passed function
class Employee():
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return '({}, {}, ${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

def e_sort(emp): # a custom func so that Python knows how to sort the list
	return emp.salary

s_employees1 = sorted(employees, key=e_sort, reverse=True)
print(s_employees1)

s_employees2 = sorted(employees, key=lambda e: e.name) # using an anonymous function
print(s_employees2)

from operator import attrgetter
s_employees3 = sorted(employees, key=attrgetter('age'))
print(s_employees3)