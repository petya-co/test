'''
a = (4+2)
x = (5+5)
y = (a+x)
print(y)
print("hello word")
import string

def function():
	pass
def factorial(number):
	return number * factorial( number - 1) if number != 1 else 1
number = int(input("Please enter the number:"))
print("The factorial of", number, "is", factorial(number))


lead_guitar = "Petya"
drums = "Sveta"
bass_and_vocalc = "Olya"
print("{}, {} and {} are in the band".format(lead_guitar, drums, bass_and_vocalc))




l = []
for inx in range(5):
	l.append(inx)

print(l)
import string

my_list = ['upper_case','lowercase','digist']
print(my_list[0])
print(my_list[-1])
print(my_list[1])
print(my_list[:-1])

#my_list = list(upper_case)
#my_list_length = len(my_list)
#print(my_list)
#for inx in range(my_list_length):
#if inx % 2 == 0:
 #  work
#digist_list = [1, 33, 55, 21, 88, 5, 8]
#for number in digist_list:
#	if number % 2 == 0:
#		print(number)

my_list = [33, 22, 'dd', 'ww', 1, 's', 3]
for number in my_list:
	if isinstance(number, str):
		print(number)
my_list = [1, 'a', None]
my_list_length = len(my_list)
for inx in range(my_list_length):
	if not isinstance(my_list[inx], str):

		my_list[inx] = str(my_list[inx])
print(my_list)
my_chars_dict = {}
for num in range(50, 100):
	my_chars_dict[num] = chr(num)
print(my_chars_dict)	
import string
import random


import string
from itertools import product
passwords = [''.join(x) for x in product(string.ascii_lowercase, repeat=1)]
print(string.ascii_lowercase)


D = dict(apple = 7)
apple = {'ret': 5, 'green' : 2}
D['apple'] =apple
print(apple)
'''
#contry_doms = {'Ukraine': 'UA'}
#d = {'UA': 'Kiev'}
#	print(d)


#my_set = {1.0, "Hello", ('*', 2, 3)}
#d = {'Hello'}
#print(d)

my_set = {'authenticated', 'googl'}
if not user
try:
authenticated = database[user] == user