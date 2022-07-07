
try:
	raise FileNotFoundError # raise an Exception
	f = open('not_existing_file.txt')
	var = bad_var
except FileNotFoundError as e:
	print(e)
except NameError as e:
	print(e)
else:
	# if no exception was caught
	print(f.read())
	f.close()
finally:
	# it runs no matter what, for closing the db/file
	print('Executing \'finally\'...')