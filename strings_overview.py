my_message1 = 'Bobby\'s message'
my_message2 = "Bobby's message"
my_message3 = """a string with
				more than 1 line"""

print(my_message1)
print(my_message2)
print(my_message3)

print(len(my_message1))

print(my_message1[0])

# slicing
print(my_message1[0:5]) # 5 is not inclusive
print(my_message1[:5])
print(my_message1[8:])

print(my_message1.lower())
print(my_message1.upper())

print(my_message1.count('message'))

print(my_message1.find('\'')) # returns the index that the character starts with
print(my_message1.find('Universe')) # -1 means no such character

temp_message = "Hello World"
new_message = temp_message.replace('World', 'Universe') # returns a new string
print(new_message)

# concatenation
greeting = 'Hello'
name = 'Michael'
message1 = greeting + ', ' + name+ '. Welcome!'
print(message1)
message2 = '{0}, {1}. Welcome!'.format(greeting, name) # {} are placeholders
print(message2)
message3 = f'{greeting}, {name.upper()}. Welcome!' # f-strings
print(message3)

print(dir(my_message1)) # shows all the attributes and methods that we have with the variable

print(help(str)) # shows the information with the passed type