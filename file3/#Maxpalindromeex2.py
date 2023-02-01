#Maxpalindromeex2.py
lst=[ "mom","madam","liril","malayalam","racecar"]
cl=0
ml=0
for i in range(0,len(lst)):
	cv=lst[i]
	if(cv==cv[::-1]):
		cl=len(cv)
	if(cl>ml):
		ml=cl
		pos=i
else:
	print(lst[pos])
