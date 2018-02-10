
# s = input("Input a string")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)


star = '*'
loop_number = 5
for  i in range(loop_number):
	for j in range(i):
		print(star, end=u'хуйня')
	print()