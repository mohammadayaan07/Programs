#Write a Python program to get the largest number from a list. 
#big.py
lst=[12,400005,389,23,100,90000000]
bg=lst[0]

for i in range(1,len(lst)):
	if bg<lst[i]:
		bg=lst[i]
	else:
		bg
print(bg)
lst=[12,400005,3008989,23,100,9000]
bg=lst[0]

for i in range(1,len(lst)):
	if bg>lst[i]:
		st=bg
	else:
		st=lst[i]
		bg=lst[i]
print(st)
5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
		Sample List : ['abc', 'xyz', 'aba', '1221']
		Expected Result : 2