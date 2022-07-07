
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['courses'])

print(student.get('email', 'Not found'))

student['phone'] = '555-5555'
print(student.get('phone'))

student.update({'name': 'Jane', 'email': 'jane94@gmail.com'})
print(student)

del student['age']
print(student)

email = student.pop('email')
print(email)
print(student)

print(len(student))

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
	print(key, value)