
sentence1 = "My name is {name} and I'm {age} years old".format(name='Jehn', age='30')
print(sentence1)

for i in range(1, 11):
	sentence2 = 'The value is {:03}'.format(i)
	print(sentence2)

pi = 3.14159265
sentence3 = 'Pi is equal to {:.2f}'.format(pi)
print(sentence3)

sentence4 = '1 Mb is equal to {:,.2f}'.format(1000**2)
print(sentence4)

import datetime
my_date = datetime.datetime(2002, 8, 30, 20, 00, 30) # 2016-09-24 12:30:45
sentence5 = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence5)