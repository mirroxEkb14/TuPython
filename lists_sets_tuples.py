# --- Lists ---

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses[0:2]) # 2 is not included

courses.append('Art')
courses.insert(0, 'Geography')
print(courses)
courses_2 = ['Education', 'Chemie']
courses.insert(0, courses_2)
print(courses)

courses.extend(courses_2)
print(courses)

courses.remove('Math')
popped = courses.pop() # always in the end and returns a removed value
print(courses)
print(popped)

courses.reverse()
print(courses)

# it's altering the list (the original one changes)
characters = ['c', 'b', 'a']
numbers = [3, 2, 1]
characters.sort() # in alphabetical order
numbers.sort() # in ascending order
print(characters)
print(numbers)
numbers.sort(reverse=True) # in descending order
print(numbers)

# use 'sorted' function so that the original list is not altering
sorted_characters = sorted(characters) # returns a sorted version of the list
print(sorted_characters)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

print(courses.index('CompSci')) # get an index of the value

print('Art' in courses)

for index, course in enumerate(courses, start=1):
	print(index, course)

characters_str = ', '.join(characters)
print(characters_str)

characters_list = characters_str.split(', ')
print(characters_list)

# --- Tuples ---

# we cannot modify tuples (immutable)
tuple1 = ('History', 'Math', 'Physics', 'CompSci')
print(tuple1)

# --- Sets ---

# sets throw away duplicates, do not save the order, more optimazed
set1 = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(set1)

set2 = {'History', 'Math', 'Art', 'Design'}
print(set1.intersection(set2)) # shows what is in both sets
print(set1.difference(set2)) # returns what what set1 has and set2 does not
print(set1.union(set2)) # unite both sets

# empty lists, tuples, sets
empty_list1 = []
empty_list2 = list()

empty_tuple1 = ()
empty_tuple2 = tuple()

empty_set = set()