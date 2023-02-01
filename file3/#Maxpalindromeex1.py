#Maxpalindromeex1.py
lst=[ 1, 232, 5545455, 999999, 1212 , 8558 ]
cl=0
ml=0
pos=-1
for i in range(0,len(lst)):
	cv=str(lst[i])
	if(cv==cv[::-1]):
		cl=len(cv)
	if(cl>ml):
			ml=cl
			pos=i
else:
	print("Max palindrome value ={}".format(lst[pos]))
