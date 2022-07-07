'''
LEGB
Local -> in a function
Enclosing -> in the local scope of enclosing functions
Global -> at the top level of a module
Built-in -> names that are preassigned in Python
'''

# in the main body of a file
x = 'global x'
# it's local to the function
def test():
	y = 'local y'


# here we tell Python that we want to change the global c-variable inside the function
c = 'global c'
def change_c():
	global c
	c = 'local c'
	print(c)
change_c()
print(c)

# min-functuon is built-in
m = min([5, 1, 4, 2, 3])
print(m)
# get all built-in functions
import builtins
print(dir(builtins)) # dir-function gets the list of attributes of the passing argument


# enclosing example(only in nested functions)
def outer():
	x = 'outer x'

	def inner():
		nonlocal x # change x in the outer func
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()