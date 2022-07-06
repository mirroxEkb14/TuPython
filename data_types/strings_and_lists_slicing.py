
# list[start:end:step], end is non-inclusive
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[2:-1:2])
print(my_list[-1:0:-2])
print(my_list[::-1])

# reverse
sample_url = 'http://coreyms.com'
print(sample_url[::-1])

# get the top level domain
print(sample_url[-4:])

# print without 'http://'
print(sample_url[7:])

# print without 'http://' and '.com'
print(sample_url[7:-4])