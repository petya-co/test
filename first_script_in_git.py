
n=5;
for i in range(n):
    for j in range(i):
        print('* ',end="") 
    print('')


for i in range(n,0,-1):
    for j in range(i):
        print('* ',end="")
    print('')
'''

# chotnoe ne chotnoe
#numbers = (1, 2, 3, 4, 5, 6, 7, 8)
#count_even=0
#count_add=0
#for i in numbers:
#	
#	print(count_even)
#	print(count_add)

# dva sposoba dileniya chisel na 7 i 5
'''
nl=[]   # 1 
for x in range(150, 270):
	if(x%7==0) and (x%5==0):
		nl.append(str(x))
		print(','.join(nl))

x=range(1500,2700) #  2
for i in x:
    if (i%7==0 and i%5==0): 
        print(i)

 
s = int(input('numbers'))
d=l=0
for c in s:
	if c.jsdigit():
		d=d+1
	elif c.jsalpha():
		l=l+1
	else:
		pass
print("Letters", l)
print("Digits", d)
'''
'''
row = 2 # ctroka
column = 3 # kolonka
a = [[i*j for j in range(column)] for i in range(row)]
print(a)
# variant 2 variant s vodam number

row_num = int(input("Input nuber of rows:"))
col_num = int(input("Input nuber of columns"))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for ro in range(row_num):
	for col in range(col_num):
		multi_list[row][col]= row*col

print(multi_list)

'''
'''
s = input("Input a string:")
d=l=0
for c in s:
	if c.isdigit():
		d=d+1
	elif c.isalpha():
		l=l+1
	else:
		pass
print("Letters", l)
print("Digits", d)
'''
'''
#a = input('enter:')
#b = a.split('')
#c = b[1].split('.')
#print(d)
#print(len(b[0]))
#print(c)
#print(len(c))

def calc():
	a = list()
	d = list()
	s = str(input('Enter a string:'))
	for i in s:
		if i in string.ascii_letters:
			l.append(i)
		elif i in string.digits:
			d.append(i)
print('letters:', len(l), '\n', 'Digits:', len(d))
'''

#user_name = input("user_name: ")
#password = input("Input your password: ")
#database = {
 #       'Petya': '1234',
  #      'Anton': '234'
#}
#if not user_name
#try:
#	authenticated = database[user_name] == password
#except KeyError:
import re

lines = ['тест', 'Call', 'string', 'box', 'cute']

for line in lines:
    if re.match(r'\b[c|с][а-яa-z]*\b', line, re.IGNORECASE):
    	
        print(line)
   