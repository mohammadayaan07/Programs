# Write a Python program to get the smallest number from a list.
#smmllst.py
lst=[12,400005,-655,3008989,2,100,9000,0,-900]
sm=lst[0]

for i in range(1,len(lst)):
	if sm>lst[i]:
		sm=lst[i]
	else:
		sm
print(sm)