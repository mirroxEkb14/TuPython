
language = 'Java'
if language == 'Python':
	print('The language is Pyhton')
elif language == 'Java':
	print('The language is Java')
else:
	print('No match')

# and, or, not
user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Bad Creds')
logged_in = False
if not logged_in:
	print('Please, Log In')
else:
	print('Welcome!')

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)
b = a
print(a is b)

# False values
condition_false = False
condition_none = None
contidion_zero = 0
condition_empty_sequence = [] # '', (), []
condition_empty_mapping = {}
if condition_false or condition_none or contidion_zero or condition_empty_sequence or condition_empty_mapping:
	print('Evaluated to True')
else:
	print('Evaluated to False')