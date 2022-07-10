""" when Python runs the python-file, it sets few special variables
like '__name__' and when Python runs the file directly it sets '__name__' to '__main__',
but when we import modules, it sets '__name__' to a file name(main_name)
"""

print "This will always be run"

def main():
	print('running directly')

# if this file is running directly through Python or it's been imported
if __name__ == '__main__':
	main()