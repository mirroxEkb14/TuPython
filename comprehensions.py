
# ------------------------------------------------------------ #
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

""" I want 'n' for each 'n' in nums """
# usual method
my_list1 = []
for n in nums:
	my_list1.append(n)
print(my_list1)
# list comprehension
my_list1_alt = [n for n in nums]
print(my_list1_alt)

""" I want 'n*n' for each 'n' in nums """
# usual method
my_list2 = []
for n in nums:
	my_list2.append(n*n)
print(my_list2)
# list comprehension
my_list2_alt = [n*n for n in nums]
print(my_list2_alt)

""" I want 'n' for each 'n' in nums if 'n' is even"""
# usual method
my_list3 = []
for n in nums:
	if n % 2 == 0:
		my_list3.append(n)
print(my_list3)
# list comprehension
my_list3_alt = [n for n in nums if n % 2 == 0]
print(my_list3_alt)

# ------------------------------------------------------------ #
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

""" I want a dict{'name': 'hero'} for each name,hero in zip(names, heroes) """
my_dict1 = {}
for name, hero in zip(names, heroes):
	my_dict1[name] = hero
print(my_dict1)
# dictionary comprehension
my_dict1_alt = {name: hero for name, hero in zip(names, heroes)}
print(my_dict1_alt)

# ------------------------------------------------------------ #
nums_list = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]

""" I want a set of the list(nums without duplicates) """
nums_set = set()
for n in nums:
	nums_set.add(n)
print(nums_set)
# set comprehension
nums_set_alt = {n for n in nums}
print(nums_set_alt)